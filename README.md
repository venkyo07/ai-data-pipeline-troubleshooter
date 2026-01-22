# AI Data Pipeline Troubleshooter

An AI-powered backend service that analyzes **real-world data engineering logs** (Spark, Airflow, YARN), classifies failures, and explains **root cause + remediation steps** using a combination of **rule-based logic, Retrieval-Augmented Generation (RAG), and a local LLM**.

This project is intentionally built as a **realistic internal tool prototype**, not a toy demo.

---

## 🚀 Why This Project

Debugging distributed data systems is time-consuming and often requires deep experience. Logs are noisy, unstructured, and error messages are rarely actionable.

This project explores how AI can **assist** (not replace) engineers by:

* Cleaning and structuring raw logs
* Detecting common failure patterns deterministically
* Using AI only where it adds value (explanations & guidance)
* Falling back safely when AI is uncertain

---

## 🧠 High-Level Architecture

```
Client (API / curl / Swagger)
        ↓
FastAPI
        ↓
Log Parser & Classifier (rule-based)
        ↓
RAG (known issues / runbook knowledge)
        ↓
Local LLM (Ollama + Mistral)
        ↓
Structured JSON Response
```

---

## ✨ Features

* Supports **long, noisy logs** (INFO / WARN / ERROR mixed)
* Rule-based error classification (OOM, DAG failure, resource limits, etc.)
* Retrieval-Augmented Generation using known issues
* Free **local LLM** (no paid APIs, no data leakage)
* Deterministic handling for unknown errors
* Graceful failure handling (no crashes)
* Clean REST API with automatic documentation

---

## 🛠️ Tech Stack

* **Python 3.10**
* **FastAPI** (API layer)
* **Ollama + Mistral** (local LLM)
* **Rule-based parsing & classification**
* **RAG (JSON-based knowledge store)**
* **Structured logging**

---

## 📂 Project Structure

```
ai-data-pipeline-troubleshooter/
├── src/
│   ├── api/        # FastAPI app
│   ├── parser/    # Log cleaning & classification
│   ├── llm/       # LLM client & pipeline
│   ├── rag/       # Knowledge base & retrieval
│   └── utils/     # Logging & helpers
├── data/
│   ├── sample_logs/
│   └── known_issues.json
├── tests/
├── test_parser.py
├── test_ai_pipeline.py
└── README.md
```

---

## ⚙️ Setup & Run

### 1️⃣ Prerequisites

* Python 3.10+
* Ollama installed → [https://ollama.com](https://ollama.com)

Pull the model:

```bash
ollama pull mistral
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Start Ollama

```bash
ollama run mistral
```

(Keep this running in the background)

---

### 4️⃣ Run the API

From **project root**:

```bash
python -m uvicorn src.api.app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example API Request

```json
{
  "log": "java.lang.OutOfMemoryError: Java heap space"
}
```

### Example Response

```json
{
  "error_type": "OOM_ERROR",
  "explanation": "The Spark executor ran out of heap memory.",
  "root_cause": "Insufficient executor memory for the workload.",
  "resolution": "Increase spark.executor.memory or optimize the job."
}
```

---

## 🧯 Design Principles

* **Deterministic first, AI second**
* AI is used for **explanation**, not decision-making
* UNKNOWN errors handled without AI to avoid hallucination
* Failures are visible and recoverable
* Simple > clever

---

## 🔮 Future Improvements

* Vector-based RAG (FAISS / embeddings)
* Support for more platforms (Kafka, Hive, Presto)
* Authentication & rate limiting
* Async LLM calls
* UI for log upload & visualization

---

## 📌 Disclaimer

This is a **learning and experimentation project**, not a production-ready system. The focus is on architecture, reliability, and engineering discipline.

---

## 👤 Author

Built by a data engineer exploring **AI-assisted troubleshooting** through hands-on system design.

