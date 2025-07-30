# ClinOmics AI Pro

An AI-powered bioinformatics SaaS tool for gene expression analysis, mutation insights, drug matches, and clinical trials, with PDF reporting.

## Features

- ✅ Expression, mutation, drug, and clinical trial data for queried genes.
- ✅ Streamlit interactive UI + PDF download.
- ✅ Reliable local data for demo and launch.
- ✅ Ready for SaaS expansion and monetization.

## Setup / Launch

```bash
git clone <repo_url>
cd ClinOmics-AI-Pro
pip install -r requirements.txt

# Start FastAPI backend (needed)
uvicorn api.main:app --host 0.0.0.0 --port 10000

# In another terminal: Streamlit UI
streamlit run app.py
# ClinOmicsAI-Pro
