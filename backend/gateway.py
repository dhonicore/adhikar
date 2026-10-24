import json, uuid, datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

with open("rules.json") as f:
    RULES = json.load(f)

class AnalyseRequest(BaseModel):
    scheme: str
    status: str
    stated_reason: str
    cert_issue_date: str
    issuing_authority: str
    family_income: int
    income_proof_type: str

class GrievanceRequest(BaseModel):
    case_id: str
    scheme: str
    ground_ids: list[str]
    clause_refs: list[str]
    draft_text: str
    attachments: list[str] = []

@app.get("/rules/{scheme}")
def get_rules(scheme: str):
    if scheme not in RULES["schemes"]:
        raise HTTPException(404, "scheme not found")
    return RULES["schemes"][scheme]

@app.post("/analyse")
def analyse(req: AnalyseRequest):
    scheme = RULES["schemes"].get(req.scheme)
    if not scheme:
        raise HTTPException(404, "scheme not found")

    grounds, refs, cites = [], [], []
    outcome = "NO_GROUNDS"

    issue = datetime.date.fromisoformat(req.cert_issue_date)
    months_old = (datetime.date.today() - issue).days / 30
    cert_valid = months_old <= scheme["income_proof"]["validity_months"]
    authority_ok = req.issuing_authority in scheme["income_proof"]["issuing_authorities"]
    itr_ok = (req.income_proof_type == "itr" and req.family_income <= scheme["income_ceiling"])

    if not cert_valid:
        outcome = "NO_GROUNDS"
    elif not authority_ok:
        outcome = "FIX_AND_RESUBMIT"
    else:
        outcome = "APPEAL"
        grounds = ["R1_cert_validity", "R2_authority"]
        refs = [scheme["rules"][0]["clause_ref"], scheme["rules"][1]["clause_ref"]]
        if itr_ok:
            grounds.append("G1_itr_equivalent")
            cites.append(scheme["precedents"][0]["citation"])

    return {
        "outcome": outcome,
        "ground_ids": grounds,
        "clause_refs": refs,
        "citations": cites,
        "facts_verified": {"cert_issue_date": req.cert_issue_date, "issuing_authority": req.issuing_authority},
        "facts_unverified": ["document authenticity (self-reported in prototype)"]
    }

@app.post("/grievance")
def grievance(req: GrievanceRequest):
    year = datetime.date.today().year
    ref = f"SCHLR/E/{year}/{uuid.uuid4().int % 10000:04d}"
    return {
        "reference_id": ref,
        "status": "submitted",
        "sla_days": 7,
        "assigned_office": "District Scholarship Officer",
        "sandbox": True
    }