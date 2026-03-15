🏥 MediRAG – Multi-Agent AI Medical Report Analyzer

MediRAG is an AI-powered system that analyzes medical reports, lab results, and prescriptions using Document AI, Multi-Agent Systems, Retrieval-Augmented Generation (RAG), and LLM reasoning.

Users can upload:

📄 PDF medical reports

🖼️ Scanned image reports

💊 Doctor prescriptions

🧪 Lab test results

The system automatically extracts medical values, analyzes them, and explains the report in simple language.

🚀 Features

✔ Document AI (PDF + OCR support)
✔ Multi-Agent workflow
✔ Medical entity extraction
✔ Patient information extraction
✔ Automated medical analysis
✔ AI-generated health explanations
✔ Vector database storage
✔ Report retrieval using Report ID

🧠 System Architecture

The system uses a multi-agent pipeline built with LangGraph.

User Uploads Medical Report
        │
        ▼
Document Reader
(PDF Parser / OCR)
        │
        ▼
Agent 1 → File Classifier
        │
        ▼
Agent 2 → Medical Entity Extractor
        │
        ▼
Agent 3 → Patient Info Extractor
        │
        ▼
Agent 4 → Medical Analysis Agent
        │
        ▼
Agent 5 → Response Generator
        │
        ▼
Vector Database Storage
        │
        ▼
User Receives Medical Explanation
📂 Project Structure
medirag-ai/
│
├── agents/
│   ├── classifier_agent.py
│   ├── entity_extractor_agent.py
│   ├── patient_info_agent.py
│   ├── analysis_agent.py
│   └── response_agent.py
│
├── rag/
│   ├── embedding_model.py
│   ├── vector_store.py
│   └── retrieval_agent.py
│
├── utils/
│   ├── pdf_reader.py
│   ├── ocr_reader.py
│   └── report_id_generator.py
│
├── workflows/
│   └── medical_workflow.py
│
├── config/
│   └── settings.py
│
├── database/
│   └── chroma_db/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
🧰 Technology Stack
Backend

Python

FastAPI / Streamlit

Multi-Agent System

LangGraph

LLM

Groq

Llama 3 / Mixtral models

Document Processing

PyPDF

OCR using Tesseract

Embeddings

Sentence Transformers

Vector Database

ChromaDB

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/medirag-ai.git

cd medirag-ai
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add API Key

Create .env file

GROQ_API_KEY=your_api_key_here
▶ Running the Application

Run the Streamlit application:

streamlit run app.py

Open browser:

http://localhost:8501
📄 Example Medical Values Extracted

Example output:

{
 "hemoglobin": 10.5,
 "blood_sugar": 113,
 "platelets": 205000,
 "cholesterol": 194
}
📊 Medical Analysis Example
Hemoglobin → Low (Possible anemia)

Blood Sugar → Slightly High

Cholesterol → Near upper limit
🔑 Report ID Storage

After analysis, each report is stored in the vector database.

Example:

Report ID: MED-a73b9f21

Users can later retrieve their report using this ID.

🔍 Retrieval Using RAG

Using Retrieval-Augmented Generation, the system can answer questions like:

What does my hemoglobin level mean?

The AI retrieves the stored report and explains it.

⚠ Medical Disclaimer

This system is intended for educational and informational purposes only.

It does not replace professional medical advice.
Users should always consult a qualified healthcare professional for diagnosis and treatment.

📈 Future Improvements

Planned upgrades:

Prescription understanding agent

Chat with medical reports

Medical knowledge RAG (WHO guidelines)

Deployment to cloud

Doctor recommendation system

👨‍💻 Author

Uppala Venkata Satya Srinivas

Data Science & AI Enthusiast

Portfolio
https://srinuuppala.netlify.app/

LinkedIn
https://www.linkedin.com/in/srinuuppala/

⭐ If this project helped you

Please ⭐ star the repository on GitHub.