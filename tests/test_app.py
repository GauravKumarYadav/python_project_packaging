from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from fastapiproject.app import app, CustomModel

client = TestClient(app)

subprocess_mock = MagicMock()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@patch("fastapiproject.app.subprocess")
def test_read_hive(subprocess_mock):
    subprocess_mock.check_output.return_value = b"30\tTestUser\ttest@example.com\n"
    response = client.get("/get_from_hive")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == 200
    assert data["size"] == 1
    assert data["data"][0] == {
        'age': '30',
        'name': 'TestUser',
        'email': 'test@example.com'
    }


@patch("fastapiproject.app.subprocess")
def test_read_hive_error(subprocess_mock):
    subprocess_mock.check_output.side_effect = Exception("Hive error")
    response = client.get("/get_from_hive")
    assert response.status_code == 500

@patch("fastapiproject.app.subprocess")
def test_insert_into_hive(subprocess_mock):
    subprocess_mock.check_output.side_effect = [b'',b"TestUser\t30\ttest@email.com\n"]
    payload = {
        "name": "TestUser",
        "age": 30,
        "email": "test@email.com"
    }
    response = client.post("/post_into_hive", json=payload)
    assert subprocess_mock.check_output.call_count == 2
    print(response.json())
    assert response.json() == {"message": "Data written to Hive successfully"}
    assert response.status_code == 200


@patch("fastapiproject.app.subprocess")
def test_insert_into_error(subprocess_mock):
    subprocess_mock.check_output.side_effect = Exception("Hive error")
    payload = {
        "name": "TestUser",
        "age": 30,
        "email": "test@example.com"
    }
    response = client.post("/post_into_hive", json=payload)
    print(response.json())
    assert response.status_code == 500
