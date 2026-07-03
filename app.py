import streamlit as st
import requests
import pandas as pd

st.title("MechanicMind — Offline Diagnostic Copilot")

with open("manual.txt") as f:
    manual_text = f.read()

sensor_df = pd.read_csv("sensor_log.csv")

def ask_ai(question):
    prompt = f"""You are a heavy machinery diagnostic assistant.
Use ONLY the information below to answer.

MANUAL/FAULT CODES:
{manual_text}

RECENT SENSOR LOG:
{sensor_df.to_string()}

TECHNICIAN QUESTION: {question}

Give: likely cause, confidence (High/Medium/Low), and recommended action."""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "phi3", "prompt": prompt, "stream": False}
    )
    return response.json()["response"]

question = st.text_input("Ask a diagnostic question:")
if st.button("Diagnose") and question:
    with st.spinner("Thinking (fully offline)..."):
        answer = ask_ai(question)
    st.write(answer)

    with open("reports.log", "a") as f:
        f.write(f"Q: {question}\nA: {answer}\n---\n")