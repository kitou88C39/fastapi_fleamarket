from fastapi.testclient import TestClient


def test_find_all(client_fixture: TestClient):
    response = client_fixture.get("/items")
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 2


def test_find_by_id_SuccessCase(client_fixture: TestClient):
    response = client_fixture.get("/items/1")
    assert response.status_code == 200
    items = response.json()
    assert items["id"] == 1