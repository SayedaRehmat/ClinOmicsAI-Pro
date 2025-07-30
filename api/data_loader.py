import pandas as pd
import json
from pathlib import Path

BASE = Path(__file__).parent.parent / "data"

def load_expression(gene: str):
    df = pd.read_csv(BASE / "expression.csv")
    rec = df[df["gene"] == gene.upper()]
    return rec.iloc[0].to_dict() if not rec.empty else {"error": "Expression not found"}

def load_mutations(gene: str):
    df = pd.read_csv(BASE / "mutations.csv")
    matches = df[df["gene"] == gene.upper()]
    return matches.to_dict(orient="records") if not matches.empty else []

def load_drugs(gene: str):
    with open(BASE / "drugs.json") as f:
        data = json.load(f)
    return data.get(gene.upper(), [])

def load_trials(gene: str):
    with open(BASE / "trials.json") as f:
        data = json.load(f)
    return data.get(gene.upper(), [])

