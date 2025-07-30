import streamlit as st
import requests

API_URL = "https://clinomicsai-pro.onrender.com"

st.title("ClinOmics AI")

gene = st.text_input("Gene Symbol", "")
if st.button("Analyze") and gene:
    st.write("Fetching...")
    try:
        expr = requests.get(f"{API_URL}/expression/{gene}", timeout=5).json()
        st.json(expr)
    except Exception as e:
        st.error(f"API Error: {e}")
