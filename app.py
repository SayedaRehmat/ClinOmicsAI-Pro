# app.py
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

BASE_API = "https://clinomics-ai.onrender.com"  # Your FastAPI URL

st.set_page_config(page_title="ClinOmics AI Pro", layout="wide")

st.title("🧬 ClinOmics AI Pro")
st.subheader("AI-powered gene mutation analysis, drug discovery, and clinical trial insights")

with st.sidebar:
    st.header("🔍 Search")
    gene = st.text_input("Gene Symbol (e.g., TP53)", "TP53")
    if st.button("Analyze"):
        st.session_state.query = gene.upper()

if "query" in st.session_state:
    gene = st.session_state.query

    st.markdown(f"## Results for `{gene}`")

    col1, col2 = st.columns(2)
    
    try:
        expr = requests.get(f"{BASE_API}/expression/{gene}").json()
        if "error" in expr:
            col1.warning(expr["error"])
        else:
            df_expr = pd.DataFrame([expr])
            col1.subheader("📊 Gene Expression")
            col1.dataframe(df_expr)
            df_expr.set_index("gene").T.plot(kind='bar', legend=False, ax=col1)
            col1.pyplot(plt.gcf())

    except Exception as e:
        col1.error(f"Expression API failed: {e}")

    try:
        muts = requests.get(f"{BASE_API}/mutations/{gene}").json()
        if muts:
            df_muts = pd.DataFrame(muts)
            col2.subheader("🧬 Mutations")
            col2.dataframe(df_muts)
        else:
            col2.warning("No mutation data found.")

    except Exception as e:
        col2.error(f"Mutation API failed: {e}")

    st.markdown("---")
    st.subheader("💊 Drug Matches")
    try:
        drugs = requests.get(f"{BASE_API}/drugs/{gene}").json()
        if drugs:
            st.table(pd.DataFrame(drugs))
        else:
            st.warning("No drug data found.")
    except Exception as e:
        st.error(f"Drug API failed: {e}")

    st.subheader("📋 Clinical Trials")
    try:
        trials = requests.get(f"{BASE_API}/trials/{gene}").json()
        if trials:
            df_trials = pd.DataFrame(trials)
            st.dataframe(df_trials)
        else:
            st.warning("No clinical trials found.")
    except Exception as e:
        st.error(f"ClinicalTrials API failed: {e}")

    st.markdown("---")
    if st.button("📥 Download PDF Report"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"ClinOmics AI Pro Report for {gene}", ln=True, align='C')
        pdf.ln(10)

        if expr:
            pdf.cell(200, 10, txt="Gene Expression:", ln=True)
            for k, v in expr.items():
                pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
        pdf.ln(5)

        if muts:
            pdf.cell(200, 10, txt="Mutations:", ln=True)
            for m in muts:
                pdf.cell(200, 10, txt=f"{m['mutation']} - {m['impact']}", ln=True)
        pdf.ln(5)

        if drugs:
            pdf.cell(200, 10, txt="Drugs:", ln=True)
            for d in drugs:
                pdf.cell(200, 10, txt=f"{d['name']} ({d['status']})", ln=True)
        pdf.ln(5)

        if trials:
            pdf.cell(200, 10, txt="Clinical Trials:", ln=True)
            for t in trials:
                pdf.cell(200, 10, txt=f"{t['title']} - {t['country']}", ln=True)

        filename = f"{gene}_report.pdf"
        pdf.output(filename)
        with open(filename, "rb") as f:
            st.download_button("Download PDF", f, file_name=filename, mime="application/pdf")

