from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# 1️⃣ Define the app first
app = FastAPI()

# 2️⃣ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev, allow all. Later restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3️⃣ Define Pydantic request schema
class ChatRequest(BaseModel):
    message: str

# 4️⃣ Test root route
@app.get("/")
def root():
    return {"status": "Backend is running 🚀"}

# 5️⃣ Chat route
@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "response": f"You said: {req.message}"
    }
    