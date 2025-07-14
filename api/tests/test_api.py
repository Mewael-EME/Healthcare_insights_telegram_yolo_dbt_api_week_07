# api/tests/test_api.py
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_top_products_requires_key():
    response = client.get("/api/reports/top-products")
    assert response.status_code == 403

def test_top_products():
    response = client.get("/api/reports/top-products", headers={"X-API-Key": "2328"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
