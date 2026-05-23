from fastapi import FastAPI
from pydantic import BaseModel
from backend.ai import messaging

app = FastAPI()

class TestData(BaseModel):
    status: bool
    data: str

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": "0.1"
    }

@app.post("/ai/send_request")
def send_request(data: TestData):
    return messaging.send_request(data.data)