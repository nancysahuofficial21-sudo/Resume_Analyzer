from fastapi import FastAPI, UploadFile, File, Form
from services.parser import extract_text
from services.extractor import extract_info
from services.analyzer import analyze_resume
from services.ai_feedback import generate_feedback
from services.matcher import match_resume

app = FastAPI()

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...), job_description: str = Form("")):
    
    text = extract_text(file)
    info = extract_info(text)
    analysis = analyze_resume(text)
    feedback = generate_feedback(text)
    match = match_resume(text, job_description) if job_description else {}


    return {
        "candidate_profile": info,
        "analysis": analysis,
        "recommendations": feedback,
        "match": match
    }