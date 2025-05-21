import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_users_status_code():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert "name" in data
    assert "email" in data

def test_get_nonexistent_user():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404 or response.json() == {}
