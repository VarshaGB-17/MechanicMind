# MechanicMind — Offline AI Diagnostic Copilot for Heavy Machinery

## The Problem

Heavy machinery—such as excavators, mining rigs, and construction equipment—often operates in remote sites with unreliable or no internet connectivity. When a fault occurs, technicians typically rely on paper manuals, phone calls to experts, or cloud-based diagnostic tools that don't work offline. This leads to increased downtime, delayed repairs, and potential safety risks.

---

## The Solution

MechanicMind is a fully offline, edge-deployed AI diagnostic assistant. A technician can ask natural-language questions about a machine fault, and the system reasons through equipment manuals and sensor data entirely on the local device, with zero cloud or internet dependency.

---

## How It Works

- **Local AI Model** – Runs entirely on the device using **Ollama (Phi-3)**. No API calls or internet connection required.
- **Local Knowledge Base** – Equipment manual excerpts and known fault codes are stored locally as text files.
- **Local Sensor Log** – Simulated machine telemetry such as temperature, pressure, and vibration is processed locally.
- **AI Reasoning** – The AI cross-references the technician's query with the equipment manual and recent sensor readings to generate a diagnosis.
- **Auto Logging** – Every diagnosis is saved locally as a maintenance report for future reference.

---

## Proof of Offline Operation

MechanicMind is designed to operate completely offline. Since the AI model runs locally through Ollama, the application can generate sensor-based diagnostic suggestions without requiring an internet connection.

---

## Tech Stack

- **Python**
- **Ollama (Phi-3)** – Local Large Language Model (LLM)
- **Streamlit** – Web-based user interface
- **Pandas** – Sensor log processing
- **NumPy** – Numerical computations
- **Pure Python** – No cloud services or external APIs

---

## How to Run It

### Prerequisites

- Python 3.10 or later
- Ollama installed
- Phi-3 model downloaded

### Setup

```bash
git clone https://github.com/VarshaGB-17/MechanicMind.git
cd MechanicMind

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

ollama pull phi3
ollama serve

streamlit run app.py
```

---


## Team

- Varsha Bhooti
- Sushmitha D S


Information Science and Engineering

Nitte Meenakshi Institute of Technology

---

## License

This project was developed for educational purposes and hackathon participation.
