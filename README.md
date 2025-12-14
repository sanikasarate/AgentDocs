# 📄 AgentDocs - Multimodal AI Knowledge Assistant

**AgentDocs** is a local AI assistant capable of handling **factual queries, image analysis, and table processing**. It runs fully offline with **simulated AI responses**, requiring **no API key or paid services**.

---

## 🔑 Key Features

- **Factual Queries:** Structured answers from a local knowledge base.  
- **Image Analysis:** Simulated OCR/image processing.  
- **Table Queries:** CSV and table parsing.  
- **Chat-like UI:** Interactive frontend built with Streamlit.  
- **Modular Design:** Easy to extend with new tools and agents.

---

## 🗂 Project Structure

AgentDocs/
├── app/
│ ├── agents/ # Router & knowledge base
│ ├── rag/ # Retrieval logic
│ ├── vision/ # OCR/image logic
│ ├── tools/ # Table/CSV parsing
│ └── frontend/ # Streamlit UI
├── data/ # Optional input files
├── tests/ # Optional unit tests
├── requirements.txt
└── .gitignore

---

## ⚡ Setup & Run

```bash
# Clone the repo
git clone https://github.com/sanikasarate/AgentDocs.git
cd AgentDocs

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/frontend/app.py

💬 Example Queries
Query	Type	Output
What is Python?	factual	Simulated structured answer
sample_image.png	image	Simulated image/OCR result
sample.csv	table	Simulated table parsing result
🛠 Skills Demonstrated

Python

Modular project design

Streamlit UI development

Simulated AI/ML logic and RAG structure

👩‍💻 Author

Sanika Sarate
B.Tech in AI & Data Science, India
Note: This project is fully functional offline and ready for further AI integration in the future. No API keys are required.
