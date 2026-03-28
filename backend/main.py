from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request schema (input validation)
class ChatRequest(BaseModel):
    message: str

# Test route
@app.get("/")
def root():
    return {"status": "Backend is running 🚀"}

# Chat route
@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "response": f"You said: {req.message}"
    }