MechanicMind — Offline AI Diagnostic Copilot
The Problem
Heavy machinery — excavators, mining rigs, construction equipment — often operates in remote sites with unreliable or zero internet connectivity. When a fault occurs, technicians typically rely on paper manuals, phone calls to head office, or cloud-based diagnostic tools that simply don't work offline. This causes delays in repair, increased downtime, and safety risks.

The Solution
MechanicMind is a fully offline, edge-deployed AI diagnostic assistant. A technician can ask natural-language questions about a machine fault, and the system reasons through the equipment manual and live sensor data — entirely on-device, with zero cloud or internet dependency.

How It Works
Local AI model — runs entirely on the device via Ollama (Phi-3-mini), no API calls, no internet required
Local knowledge base — equipment manual excerpts and known fault codes stored as plain text
Local sensor log — simulated machine telemetry (pressure, temperature, vibration)
Reasoning — the AI cross-references the technician's question against both the manual and recent sensor readings to produce a diagnosis
Auto-logging — every diagnosis is saved locally as a maintenance report
Proof of Offline Operation
Tested with wifi fully disabled — the system still generates accurate, sensor-grounded diagnoses in real time.

Tech Stack
Ollama (Phi-3-mini) — local LLM inference
Streamlit — chat interface
Pandas — sensor log processing
Pure Python, no cloud services
How to Run It
Prerequisites
Python 3.10+
Ollama installed
Setup
git clone https://github.com/s-sushmitha12/mechanicmind.git
cd mechanicmind
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
ollama pull phi3
