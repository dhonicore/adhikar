import os
import json
import re
import httpx
from datetime import datetime, timezone
from uuid import uuid4
from dotenv import find_dotenv, load_dotenv
from uagents import Agent, Context, Protocol
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement, ChatMessage, TextContent, MetadataContent, chat_protocol_spec
)
from .cards import card_message, intake_form

load_dotenv(find_dotenv())

intake = Agent(
    name="intake",
    seed=os.getenv("INTAKE_SEED_PHRASE"),
    port=8001,
    mailbox=True,
    network="testnet",  # Recommended to avoid Almanac funding issues
    mailbox_api_token=os.getenv("AGENTVERSE_API_TOKEN"),  # <-- Add this line
    publish_agent_details=True,
)
chat_proto = Protocol(spec=chat_protocol_spec)

# Local FastAPI URLs
ANALYST_URL = os.getenv("ANALYST_URL", "http://127.0.0.1:8002/analyse")
DRAFTER_DRAFT_URL = os.getenv("DRAFTER_DRAFT_URL", "http://127.0.0.1:8003/draft")
DRAFTER_CONFIRM_URL = os.getenv("DRAFTER_CONFIRM_URL", "http://127.0.0.1:8003/confirm")

@chat_proto.on_message(ChatMessage)
async def handle_chat(ctx: Context, sender: str, msg: ChatMessage):
    await ctx.send(sender, ChatAcknowledgement(timestamp=datetime.now(tz=timezone.utc), acknowledged_msg_id=msg.msg_id))
    
    text = " ".join(item.text for item in msg.content if isinstance(item, TextContent))
    meta_str = "".join(json.dumps(item.metadata) for item in msg.content if isinstance(item, MetadataContent))
    full_content = text + " " + meta_str

    # 1. Route to Analyst (Form Submit)
    if "submit_intake" in full_content or ('"action"' in full_content and "draft_appeal" not in full_content and "confirm_send" not in full_content):
        ctx.logger.info("Caught Form Submission. Parsing JSON...")
        json_match = re.search(r'\{.*\}', full_content, re.DOTALL)
        if not json_match: 
            ctx.logger.error("No JSON found in form submission!")
            return
        
        try:
            case_data = json.loads(json_match.group(0))
            if "data" in case_data:
                case_data = case_data["data"] # Handle ASI:One wrapper
            case_data.pop("action", None)
            case_data.pop("approved", None)
            ctx.storage.set("current_case", json.dumps(case_data))
        except Exception as e:
            ctx.logger.error(f"Failed to parse form JSON: {e}")
            await ctx.send(sender, ChatMessage(timestamp=datetime.now(tz=timezone.utc), msg_id=uuid4(), content=[TextContent(type="text", text=f"Parse error: {e}")]))
            return
        
        await ctx.send(sender, ChatMessage(timestamp=datetime.now(tz=timezone.utc), msg_id=uuid4(), content=[TextContent(type="text", text="Checking rules...")]))
        
        # Call local Analyst
        ctx.logger.info(f"Sending to Analyst at {ANALYST_URL}...")
        async with httpx.AsyncClient() as client:
            try:
                r = await client.post(ANALYST_URL, json=case_data, timeout=60)
                result = r.json()
                ctx.logger.info(f"Analyst response: {result}")
            except Exception as e:
                ctx.logger.error(f"Failed to call Analyst: {e}")
                await ctx.send(sender, ChatMessage(timestamp=datetime.now(tz=timezone.utc), msg_id=uuid4(), content=[TextContent(type="text", text=f"Analyst error: {e}")]))
                return
        
        outcome = result.get("outcome", "NO_GROUNDS")
        title = "✅ Your rejection looks wrong!" if outcome == "APPEAL" else "❌ I cannot file an appeal"
        narration = "The rules support an appeal." if outcome == "APPEAL" else "The rejection appears correct."
        
        payload = {
            "title": title,
            "summary_rows": [
                {"label": "Outcome", "value": outcome.replace("_", " ").title()},
                {"label": "Grounds", "value": ", ".join(result.get("ground_ids", [])) or "None"},
                {"label": "Citations", "value": "; ".join(result.get("citations", [])) or "None"}
            ],
            "ctas": [{"label": "Draft Appeal Letter", "primary": True, "selection": {"action": "draft_appeal"}}]
        }
        meta = {"card_protocol_version": "1", "requires_card_interaction": "true", "card_kind": "detail", "card_payload": json.dumps(payload)}
        
        await ctx.send(sender, ChatMessage(timestamp=datetime.now(tz=timezone.utc), msg_id=uuid4(), content=[TextContent(type="text", text=narration), MetadataContent(type="metadata", metadata=meta)]))
        return

    # 2. Route to Drafter (Draft Appeal)
    if "draft_appeal" in full_content:
        ctx.logger.info("Caught Draft Appeal. Calling Drafter...")
        await ctx.send(sender, ChatMessage(timestamp=datetime.now(tz=timezone.utc), msg_id=uuid4(), content=[TextContent(type="text", text="Drafting your appeal...")]))
        
        case_json = json.loads(ctx.storage.get("current_case") or "{}")
        case_json["ground_ids"] = ["R1_cert_validity", "G1_itr_equivalent"]
        case_json["clause_refs"] = ["Clause 4.2"]
        
        async with httpx.AsyncClient() as client:
            try:
                r = await client.post(DRAFTER_DRAFT_URL, json={"case_data": case_json}, timeout=10)
                res = r.json()
                ctx.logger.info(f"Drafter response: {res}")
            except Exception as e:
                ctx.logger.error(f"Failed to call Drafter: {e}")
                await ctx.send(sender, ChatMessage(timestamp=datetime.now(tz=timezone.utc), msg_id=uuid4(), content=[TextContent(type="text", text=f"Drafter error: {e}")]))
                return
        
        ctx.storage.set("draft_text", res["draft_text"])
        ctx.storage.set("case_id", res["case_id"])
        
        # Clean the snippet so line breaks don't break the card rendering
        snippet = res["draft_text"][:100].replace("\n", " ") + "..."
        
        payload = {
            "title": "📝 Review your appeal",
            "summary_rows": [
                {"label": "Case ID", "value": res["case_id"]},
                {"label": "Destination", "value": os.getenv("INO_EMAIL")},
                {"label": "Draft Snippet", "value": snippet}
            ],
            "ctas": [{"label": "Confirm & Send Email", "primary": True, "selection": {"action": "confirm_send"}}]
        }
        meta = {"card_protocol_version": "1", "requires_card_interaction": "true", "card_kind": "detail", "card_payload": json.dumps(payload)}
        
        # Send BOTH TextContent and MetadataContent to force ASI:One to render it
        await ctx.send(sender, ChatMessage(
            timestamp=datetime.now(tz=timezone.utc), 
            msg_id=uuid4(), 
            content=[
                TextContent(type="text", text="Here is your draft. Please review and confirm."),
                MetadataContent(type="metadata", metadata=meta)
            ]
        ))
        return

    # 3. Route to Drafter (Confirm Send)
    if "confirm_send" in full_content:
        ctx.logger.info("Caught Confirm Send. Calling Drafter...")
        
        case_id = ctx.storage.get("case_id")
        draft_text = ctx.storage.get("draft_text")
        
        async with httpx.AsyncClient() as client:
            try:
                r = await client.post(DRAFTER_CONFIRM_URL, json={"case_id": case_id, "draft_text": draft_text}, timeout=15)
                ref = r.json()
                ctx.logger.info(f"Confirm response: {ref}")
            except Exception as e:
                ctx.logger.error(f"Failed to confirm: {e}")
                await ctx.send(sender, ChatMessage(timestamp=datetime.now(tz=timezone.utc), msg_id=uuid4(), content=[TextContent(type="text", text=f"Failed: {e}")]))
                return

        # Check if Drafter returned an error
        if "error" in ref:
            await ctx.send(sender, ChatMessage(timestamp=datetime.now(tz=timezone.utc), msg_id=uuid4(), content=[TextContent(type="text", text=f"⚠️ Error: {ref['error']}")]))
            return

        ref_payload = {
            "title": "✅ Appeal Filed Successfully",
            "summary_rows": [
                {"label": "Reference ID", "value": ref.get("reference_id")},
                {"label": "SLA Deadline", "value": f"{ref.get('sla_days')} days"},
                {"label": "Assigned To", "value": ref.get("assigned_office")}
            ],
            # Adding a CTA button forces ASI:One to render the card
            "ctas": [{"label": "Done", "primary": True, "selection": {"action": "done"}}]
        }
        meta = {"card_protocol_version": "1", "requires_card_interaction": "true", "card_kind": "detail", "card_payload": json.dumps(ref_payload)}
        
        # Send ONLY the final card
        await ctx.send(sender, ChatMessage(
            timestamp=datetime.now(tz=timezone.utc), 
            msg_id=uuid4(), 
            content=[
                TextContent(type="text", text="✅ Success! I have emailed the appeal to the Nodal Officer and generated your tracking number."),
                MetadataContent(type="metadata", metadata=meta)
            ]
        ))
        return

    # 4. Default: Show Form
    await ctx.send(sender, card_message("I can help you appeal this. First, a few details:", "form", intake_form()))

@chat_proto.on_message(ChatAcknowledgement)
async def handle_ack(ctx: Context, sender: str, msg: ChatAcknowledgement): pass

intake.include(chat_proto, publish_manifest=True)
if __name__ == "__main__": intake.run()