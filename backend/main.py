"""Agent Starter Kit - Main Application."""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from auth import get_current_user
from billing import check_subscription
from usage import track_usage

app = FastAPI(
    title="Agent Starter Kit",
    description="SaaS starter for AI agents",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Agent Starter Kit API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/agent/invoke")
async def invoke_agent(
    user = Depends(get_current_user),
    subscription = Depends(check_subscription)
):
    """Invoke the AI agent."""
    if not subscription["active"]:
        raise HTTPException(403, "Subscription required")
    
    track_usage(user["id"], "invoke")
    return {"result": "Agent invoked successfully"}
