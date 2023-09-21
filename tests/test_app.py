from fastapi.testclient import TestClient
from fastapiproject.app import app  # Adjust the import path as needed

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_hive():
    response = client.get("/get_from_hive")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "data" in response.json()


def test_insert_into_hive():
    payload = {
        "name": "John",
        "age": 30,
        "email": "john@example.com"
    }
    response = client.post("/post_into_hive", json=payload)
    assert response.status_code == 200
    assert "message" in response.json()
