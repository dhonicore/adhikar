import os
import json
import time
from datetime import datetime, timezone
from uuid import uuid4
from dotenv import find_dotenv, load_dotenv
from uagents import Agent, Context, Protocol
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement, ChatMessage, TextContent, MetadataContent, chat_protocol_spec
)

load_dotenv(find_dotenv())

tracker = Agent(name="tracker", seed=os.getenv("TRACKER_SEED_PHRASE"), port=8004, mailbox=True, publish_agent_details=True)
chat_proto = Protocol(spec=chat_protocol_spec)

@chat_proto.on_message(ChatMessage)
async def handle_chat(ctx: Context, sender: str, msg: ChatMessage):
    await ctx.send(sender, ChatAcknowledgement(timestamp=datetime.now(tz=timezone.utc), acknowledged_msg_id=msg.msg_id))
    text = " ".join(item.text for item in msg.content if isinstance(item, TextContent))
    
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return
        
    if data.get("action") == "start_tracking":
        case_id = data.get("case_id")
        user_addr = data.get("user_address")
        
        # Store case with a 30-second demo deadline
        ctx.storage.set(f"case_{case_id}", {
            "user": user_addr, 
            "due": time.time() + 30, 
            "escalated": False
        })
        ctx.logger.info(f"Tracking case {case_id}. Will escalate in 30 seconds.")

@chat_proto.on_message(ChatAcknowledgement)
async def handle_ack(ctx: Context, sender: str, msg: ChatAcknowledgement): pass

@tracker.on_interval(period=5.0)
async def check_deadlines(ctx: Context):
    now = time.time()
    keys = ctx.storage.get("keys") or []
    
    for key in keys:
        case = ctx.storage.get(key)
        if case and not case["escalated"] and now >= case["due"]:
            case["escalated"] = True
            ctx.storage.set(key, case)
            
            payload = {
                "title": "⚠️ SLA Deadline Passed",
                "summary_rows": [
                    {"label": "Status", "value": "No response from Officer"},
                    {"label": "Action", "value": "Escalated to State Nodal Officer"}
                ],
                "ctas": [{"label": "View Timeline", "primary": True, "selection": {"action": "status"}}]
            }
            meta = {"card_protocol_version": "1", "requires_card_interaction": "true", "card_kind": "detail", "card_payload": json.dumps(payload)}
            
            await ctx.send(case["user"], ChatMessage(
                timestamp=datetime.now(tz=timezone.utc), msg_id=uuid4(),
                content=[TextContent(type="text", text="The deadline has passed. I have escalated your case."), MetadataContent(type="metadata", metadata=meta)]
            ))

@tracker.on_event("startup")
async def startup(ctx: Context):
    # Initialize storage keys
    if not ctx.storage.get("keys"):
        ctx.storage.set("keys", [])

@chat_proto.on_message(ChatMessage)
async def track_new(ctx: Context, sender: str, msg: ChatMessage):
    pass # Handled above

tracker.include(chat_proto, publish_manifest=True)
if __name__ == "__main__": tracker.run()