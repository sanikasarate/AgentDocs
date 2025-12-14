# app/agents/router_agent.py
from .knowledge_base import knowledge_base
import difflib

def route_query(query, query_type):
    query_lower = query.lower().strip()
    
    if query_type == "factual":
        # Fuzzy match to find the closest key in the knowledge base
        closest_match = difflib.get_close_matches(query_lower, knowledge_base.keys(), n=1)
        if closest_match:
            response = knowledge_base[closest_match[0]]
            return {"type": "factual", "response": response}
        else:
            return {"type": "factual", "response": f"No information found for '{query}'."}

    elif query_type == "image":
        return {"type": "image", "response": "Simulated image processing result"}

    elif query_type == "table":
        return {"type": "table", "response": "Simulated table processing result"}

    else:
        return {"type": "other", "response": "Simulated generic response"}







