from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.data_loader import load_expression, load_mutations, load_drugs, load_trials

app = FastAPI(title="ClinOmics AI API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def welcome():
    return {"message": "ClinOmics AI API is running"}

@app.get("/expression/{gene}")
def expr(gene: str):
    return load_expression(gene)

@app.get("/mutations/{gene}")
def mutations(gene: str):
    return load_mutations(gene)

@app.get("/drugs/{gene}")
def drugs(gene: str):
    return load_drugs(gene)

@app.get("/trials/{gene}")
def trials(gene: str):
    return load_trials(gene)

