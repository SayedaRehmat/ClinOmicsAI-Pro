import streamlit as st
import requests

API_URL = "  https://clinomicsai-pro.onrender.com"  # Update with FastAPI deployment URL

st.title("🔬 ClinOmics AI - Gene Insight")

gene = st.text_input("Enter Gene Symbol (e.g., TP53):")

if gene:
    try:
        expr = requests.get(f"{API_URL}/expression/{gene}").json()
        muts = requests.get(f"{API_URL}/mutation/{gene}").json()
        drugs = requests.get(f"{API_URL}/drug/{gene}").json()

        st.subheader("🧬 Expression Data")
        st.json(expr)

        st.subheader("🔎 Mutation Data")
        st.json(muts)

        st.subheader("💊 Drug Matches")
        st.json(drugs)

    except Exception as e:
        st.error(f"API Error: {e}")
