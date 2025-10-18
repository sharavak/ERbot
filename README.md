# ERbot

**ERbot** is an AI-powered application that converts user queries about a database into **Entity-Relationship (ER) diagrams**. It features a **Streamlit frontend** for interactive use, a **FastAPI backend** for processing, and integrates with **Groq API** for AI inference. The generated diagrams use **Mermaid syntax** for visualization.

---

## Features

- Convert natural language database queries into **ER diagrams**.
- **Interactive frontend** using Streamlit.
- **FastAPI backend** to handle query processing and diagram generation.
- **Mermaid-based diagrams** for clean, shareable ER diagrams.
- **LLM integration** via Groq API.
- **Containerized deployment** with Docker and Docker Compose.

---

## Tech Stack

| Component      | Technology              |
| -------------- | ----------------------- |
| Frontend       | Streamlit               |
| Backend        | FastAPI                 |
| Diagram Engine | Mermaid                 |
| AI Inference   | Groq API                |
| Deployment     | Docker & Docker Compose |

---

## Project Structure

    ERbot/
        ├── frontend/ # Streamlit application
        ├── backend/ # FastAPI application
        ├── docker-compose.yaml
        └── README.md # Project documentation

---

## Installation

### Clone the repository

```bash
git clone https://github.com/sharavak/ERbot.git
cd ERbot
```

###  Running the Application

You can run **ERbot** either using **Docker** or **without Docker**.

---

### Option 1: Using Docker 

If **Docker** is installed, this is the quickest way to get started.

```bash

docker-compose up --build

Frontend (Streamlit) http://localhost:8501
Backend (FastAPI) http://localhost:8000
```
### Option 2: Without Docker

#### Run the frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run Home.py
```
#### Run the backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Configuration

- Add your **Groq API key** in the backend configuration (`.env`) to enable AI inference.  
- Ensure **Docker** is installed for containerized deployment.