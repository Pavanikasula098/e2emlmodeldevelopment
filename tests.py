# test_main.py
from fastapi.testclient import TestClient
from main import app  # import your FastAPI app

client = TestClient(app)

def test_read_root():
    response = client.get("/")  # call the endpoint
    assert response.status_code == 200  # check HTTP 200 OK
    assert response.json() is None  # because your function currently returns nothing
