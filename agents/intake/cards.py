import json
from datetime import datetime, timezone
from uuid import uuid4
from uagents_core.contrib.protocols.chat import (
    ChatMessage, TextContent, MetadataContent
)

def card_message(narration: str, kind: str, payload: dict, terminal=False):
    meta = {
        "card_protocol_version": "1",
        "requires_card_interaction": "true",
        "card_kind": kind,
        "card_payload": json.dumps(payload),
        "preferred_drawer_width_px": "540",
    }
    if terminal:
        meta["is_terminal"] = "true"
    return ChatMessage(
        timestamp=datetime.now(timezone.utc),
        msg_id=uuid4(),
        content=[
            TextContent(type="text", text=narration),
            MetadataContent(type="metadata", metadata=meta),
        ],
    )

def intake_form() -> dict:
    return {
        "title": "Tell me about your scholarship rejection",
        "fields": [
            {"name": "scheme", "kind": "select", "label": "Scheme", "required": True,
             "options": [{"value": "NSP_PRE_MATRIC", "label": "NSP Pre-Matric Scholarship"}]},
            {"name": "status", "kind": "select", "label": "Status", "required": True,
             "options": [{"value": "rejected", "label": "Rejected"},
                         {"value": "defective", "label": "Defective (returned for correction)"}]},
            {"name": "stated_reason", "kind": "text", "label": "What reason did they give?", "required": True},
            {"name": "cert_issue_date", "kind": "text", "label": "Certificate issue date (YYYY-MM-DD)", "required": True},
            {"name": "issuing_authority", "kind": "select", "label": "Issuing authority", "required": True,
             "options": [{"value": "Revenue Officer", "label": "Revenue Officer"},
                         {"value": "Tehsildar", "label": "Tehsildar"},
                         {"value": "SDM", "label": "SDM"}]},
            {"name": "family_income", "kind": "number", "label": "Annual family income (INR)", "required": True},
            {"name": "income_proof_type", "kind": "select", "label": "Income proof type", "required": True,
             "options": [{"value": "income_certificate", "label": "Income Certificate"},
                         {"value": "itr", "label": "ITR"}]},
        ],
        "submit_cta": {"label": "Check my case", "selection": {"action": "submit_intake"}},
    }