from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "ClinOmics AI API is running"}

@app.get("/expression/{gene}")
def expression_data(gene: str):
    # Replace with actual DB/API logic
    return {"gene": gene, "expression_level": 42.0}

@app.get("/mutation/{gene}")
def mutation_data(gene: str):
    return {"gene": gene, "mutations": ["p53-R175H", "p53-R248Q"]}

@app.get("/drug/{gene}")
def drug_matches(gene: str):
    return {"gene": gene, "drugs": ["Olaparib", "Niraparib"]}
