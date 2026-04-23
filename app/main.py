from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

classifier = pipeline("sentiment-analysis")

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(text: str):
    result = classifier(text)
    return {"text": text, "result": result}