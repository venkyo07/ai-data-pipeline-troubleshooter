from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.llm.pipeline import analyze_log_with_ai

app = FastAPI(title="AI Log Troubleshooter")


class LogRequest(BaseModel):
    log: str


class LogResponse(BaseModel):
    error_type: str
    explanation: str
    root_cause: str
    resolution: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze-log", response_model=LogResponse)
def analyze_log(request: LogRequest):
    if not request.log.strip():
        raise HTTPException(status_code=400, detail="Log cannot be empty")

    result = analyze_log_with_ai(request.log)

    return result

