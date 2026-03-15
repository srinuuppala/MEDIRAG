# 🏥 MediRAG – Multi-Agent AI Medical Report Analyzer

**MediRAG** is an AI-powered system designed to analyze **medical reports, prescriptions, and lab test results** using **Document AI, Multi-Agent Systems, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs)**.

The system automatically extracts medical data, evaluates laboratory values, and generates **simple, human-readable explanations** to help users understand their medical reports.

---

# 🚀 Key Features

✔ **Document AI Processing** – Supports PDF reports and scanned image documents
✔ **OCR Integration** – Extracts text from scanned reports using Tesseract
✔ **Multi-Agent Workflow** – Modular AI agents handle different analysis tasks
✔ **Medical Entity Extraction** – Detects lab test values and medical parameters
✔ **Patient Information Extraction** – Identifies patient details from reports
✔ **Automated Medical Analysis** – Compares results with normal medical ranges
✔ **AI-Generated Explanations** – Provides simplified health insights using LLMs
✔ **Vector Database Storage** – Stores processed reports for future retrieval
✔ **Report ID System** – Allows users to retrieve previously analyzed reports

---

# 🧠 System Architecture

MediRAG uses a **multi-agent pipeline built with LangGraph** to process medical reports step by step.

```
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
Agent 2 → Medical Entity Extraction
        │
        ▼
Agent 3 → Patient Information Extraction
        │
        ▼
Agent 4 → Medical Analysis
        │
        ▼
Agent 5 → Response Generation
        │
        ▼
Vector Database Storage
        │
        ▼
User Receives Medical Explanation
```

---

# 📂 Project Structure

```
medirag-ai/
│
├── agents/                # AI agents for different tasks
│   ├── classifier_agent.py
│   ├── entity_extractor_agent.py
│   ├── patient_info_agent.py
│   ├── analysis_agent.py
│   └── response_agent.py
│
├── rag/                   # Retrieval-Augmented Generation components
│   ├── embedding_model.py
│   ├── vector_store.py
│   └── retrieval_agent.py
│
├── utils/                 # Utility modules
│   ├── pdf_reader.py
│   ├── ocr_reader.py
│   └── report_id_generator.py
│
├── workflows/             # Multi-agent workflow orchestration
│   └── medical_workflow.py
│
├── config/                # Configuration settings
│   └── settings.py
│
├── database/
│   └── chroma_db/         # Vector database storage
│
├── app.py                 # Application entry point
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (API keys)
└── README.md
```

---

# 🧰 Technology Stack

### Backend

* Python
* FastAPI / Streamlit

### Multi-Agent Framework

* LangGraph

### Large Language Models

* Groq API
* Llama 3 / Mixtral models

### Document Processing

* PyPDF
* Tesseract OCR

### Embeddings

* Sentence Transformers

### Vector Database

* ChromaDB

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/medirag-ai.git
cd medirag-ai
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```
venv\Scripts\activate
```

**Mac / Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Key

Create a `.env` file in the project root.

```
GROQ_API_KEY=your_api_key_here
```

---

# ▶ Running the Application

Run the Streamlit application:

```
streamlit run app.py
```

Open in your browser:

```
http://localhost:8501
```

---

# 📄 Example Extracted Medical Values

Example structured output from a report:

```json
{
 "hemoglobin": 10.5,
 "blood_sugar": 113,
 "platelets": 205000,
 "cholesterol": 194
}
```

---

# 📊 Example Medical Analysis

```
Hemoglobin → Low (Possible anemia)

Blood Sugar → Slightly elevated

Cholesterol → Near upper limit
```

The system analyzes lab values against standard medical ranges and provides simplified explanations.

---

# 🔑 Report ID Storage

Each processed report is stored in the vector database with a **unique report identifier**.

Example:

```
Report ID: MED-a73b9f21
```

Users can retrieve previously analyzed reports using this ID.

---

# 🔍 Retrieval Using RAG

The system supports **Retrieval-Augmented Generation (RAG)** to answer user questions about their medical report.

Example query:

```
What does my hemoglobin level indicate?
```

The AI retrieves the stored report data and generates an explanation.

---

# ⚠ Medical Disclaimer

This project is intended **only for educational and informational purposes**.

It does **not replace professional medical advice**.
Users should always consult a qualified healthcare professional for diagnosis and treatment.

---

# 📈 Future Improvements

Planned enhancements include:

• Prescription understanding agent
• Chat interface for interacting with medical reports
• Integration with medical knowledge bases (WHO / clinical guidelines)
• Cloud deployment for public access
• Doctor recommendation system

---

# 👨‍💻 Author

**Uppala Venkata Satya Srinivas**
Data Science & AI Enthusiast

🌐 Portfolio
https://srinuuppala.netlify.app/

🔗 LinkedIn
https://www.linkedin.com/in/srinuuppala/

---

# ⭐ Support the Project

If you found this project useful, please consider **starring the repository** ⭐ on GitHub.
