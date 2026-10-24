import os
from fastapi import FastAPI
import json, smtplib, httpx, ssl
from email.message import EmailMessage
from fpdf import FPDF
from pydantic import BaseModel
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
app = FastAPI()
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:9000")
PENDING_CASES = {}

class DraftRequest(BaseModel):
    case_data: dict

class ConfirmRequest(BaseModel):
    case_id: str
    draft_text: str

def generate_pdf(text, filename):
    safe_text = text.encode('latin-1', 'replace').decode('latin-1')
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in safe_text.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)
    pdf.output(filename)

def send_email(pdf_path, case_id):
    print(f"\n--- SENDING EMAIL ---")
    print(f"FROM: {os.getenv('SMTP_EMAIL')}")
    print(f"TO: {os.getenv('INO_EMAIL')}")
    
    msg = EmailMessage()
    msg['Subject'] = f"Scholarship Appeal - Case {case_id}"
    msg['From'] = os.getenv("SMTP_EMAIL")
    msg['To'] = os.getenv("INO_EMAIL")
    msg.set_content("Please find the attached appeal letter.")
    with open(pdf_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=pdf_path)
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as s:
        s.login(os.getenv("SMTP_EMAIL"), os.getenv("SMTP_APP_PASSWORD"))
        s.send_message(msg)
    
@app.post("/draft")
def draft(req: DraftRequest):
    case_data = req.case_data
    case_id = "ADH-123456"
    draft_text = f"To the Institute Nodal Officer,\n\nI am appealing the rejection of my scholarship.\nGrounds: {', '.join(case_data.get('ground_ids', []))}\nClauses: {', '.join(case_data.get('clause_refs', []))}\n\nEnclosures: Income certificate, rejection SMS."
    PENDING_CASES[case_id] = draft_text
    return {"case_id": case_id, "draft_text": draft_text}

@app.post("/confirm")
def confirm(req: ConfirmRequest):  # <--- Notice: DEF, not ASYNC DEF
    print(f"--- NEW REQUEST: Confirming case {req.case_id} ---")
    
    # 1. Generate PDF
    try:
        pdf_path = f"/tmp/{req.case_id}.pdf"
        generate_pdf(req.draft_text, pdf_path)
        print("✅ PDF Generated.")
    except Exception as e:
        print(f"❌ PDF Failed: {e}")
        return {"error": f"PDF failed: {str(e)}"}

    # 2. Send Email
    try:
        send_email(pdf_path, req.case_id)
        print("✅ Email Sent.")
    except Exception as e:
        print(f"❌ Email Failed: {e}")
        return {"error": f"Email failed: {str(e)}"}

    # 3. Register with Backend
    try:
        with httpx.Client(timeout=5.0) as client:
            r = client.post(f"{BACKEND_URL}/grievance", json={
                "case_id": req.case_id, "scheme": "NSP_PRE_MATRIC",
                "ground_ids": ["R1"], "clause_refs": ["Clause 4.2"], "draft_text": req.draft_text
            })
            ref = r.json()
        print(f"✅ Grievance Filed: {ref}")
        return ref
    except Exception as e:
        print(f"❌ Grievance Failed: {e}")
        return {"error": f"Backend grievance failed: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)