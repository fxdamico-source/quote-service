from fastapi import FastAPI
from random import choice

app = FastAPI()

QUOTES = [
    "Simplicity scales.",
    "Make it work, make it right, make it fast.",
    "Ship small, iterate fast.",
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/quote")
def get_quote():
    return {"quote": choice(QUOTES)}