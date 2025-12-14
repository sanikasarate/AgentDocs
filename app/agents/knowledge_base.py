# app/agents/knowledge_base.py

# A simple local knowledge base for factual queries
knowledge_base = {
    "what is python": "Python is a high-level, interpreted programming language known for its readability and versatility.",
    "what is ai": "Artificial Intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and learn.",
    "what is machine learning": "Machine Learning is a subset of AI that allows systems to learn from data and improve performance without explicit programming.",
    # Add more Q&A as needed
}

def get_factual_answer(query: str) -> str:
    """
    Returns the answer from the knowledge base if it exists.
    Performs a case-insensitive match.
    """
    query_lower = query.lower()
    return knowledge_base.get(query_lower, None)
