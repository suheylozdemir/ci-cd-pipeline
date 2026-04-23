from fastapi.testclient import TestClient  # FastAPI's built-in test tool
from app.main import app  # import our app object

client = TestClient(app)  # create a test client, works like a browser

def test_health_check():
    response = client.get("/")  # send GET request to /
    assert response.status_code == 200  # expect success response
    assert response.json() == {"status": "ok"}  # expect this exact response

def test_predict_positive():
    response = client.post("/predict?text=I love this product")  # send positive text
    assert response.status_code == 200  # expect success
    assert response.json()["result"][0]["label"] == "POSITIVE"  # expect POSITIVE label

def test_predict_negative():
    response = client.post("/predict?text=I hate this product")  # send negative text
    assert response.status_code == 200  # expect success
    assert response.json()["result"][0]["label"] == "NEGATIVE"  # expect NEGATIVE label