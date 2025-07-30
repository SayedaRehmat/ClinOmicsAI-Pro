import streamlit as st
import requests

API_URL = "https://clinomicsai-pro.onrender.com"

st.set_page_config(page_title="ClinOmics AI", page_icon="🧬")
st.title("🔬 ClinOmics AI - Gene Insight")

st.markdown("""
Type a gene (e.g., TP53, BRCA1) to fetch:
- 🧬 Gene Expression Data
- 🔎 Mutation Details
- 💊 Drug Matches
""")

gene = st.text_input("Enter Gene Symbol:", placeholder="e.g., TP53")

if gene:
    with st.spinner("Fetching data..."):
        try:
            expr = requests.get(f"{API_URL}/expression/{gene}").json()
            muts = requests.get(f"{API_URL}/mutation/{gene}").json()
            drugs = requests.get(f"{API_URL}/drug/{gene}").json()

            st.subheader("🧬 Gene Expression")
            st.json(expr if expr else {"warning": "No expression data."})

            st.subheader("🔎 Mutations")
            st.json(muts if muts else {"warning": "No mutation data."})

            st.subheader("💊 Drug Matches")
            st.json(drugs if drugs else {"warning": "No drug matches."})

        except Exception as e:
            st.error(f"API Error: {e}")
