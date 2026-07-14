"""Usage tracking module."""

from datetime import datetime
from collections import defaultdict

usage_store = defaultdict(lambda: {"count": 0, "history": []})

def track_usage(user_id: str, action: str):
    """Track user API usage."""
    usage_store[user_id]["count"] += 1
    usage_store[user_id]["history"].append({
        "action": action,
        "timestamp": datetime.utcnow().isoformat()
    })

def get_usage(user_id: str) -> dict:
    """Get user usage stats."""
    data = usage_store[user_id]
    return {
        "total_requests": data["count"],
        "recent_actions": data["history"][-10:]
    }
