# app/frontend/app.py
import streamlit as st
import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from app.agents.router_agent import route_query

st.set_page_config(page_title="AgentDocs", page_icon="📄")
st.title("📄 AgentDocs - Multimodal AI Knowledge Assistant")
st.subheader("Frontend connected to Router Agent")

# Session state to store conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
query = st.text_input("Enter your query:")
query_type = st.selectbox("Select query type:", ["factual", "image", "table", "other"])

if st.button("Submit") and query:
    response = route_query(query, query_type)
    st.session_state.history.append({"user": query, "agent": response["response"]})

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**AgentDocs:** {chat['agent']}")
    st.markdown("---")









