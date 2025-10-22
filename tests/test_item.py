from fastapi.testclient import TestClient


def test_find_all(client_fixture: TestClient):
    response = client_fixture.get("/items")
    assert response.status_code == 200
    item = response.json()
    assert len(item) == 2


def test_find_by_id_SuccessCase(client_fixture: TestClient):
    response = client_fixture.get("/items/1")
    assert response.status_code == 200
    item = response.json()
    assert item["id"] == 1


def test_find_by_id_ErrorCase(client_fixture: TestClient):
    response = client_fixture.get("/items/10")
    assert response.status_code == 404
    item = response.json()["detail"] == "Item not found"


def test_find_by_id_name(client_fixture: TestClient):
    response = client_fixture.get("/items/?name=PC1")
    assert response.status_code == 200
    item = response.json()
    assert len(item) == 1
    assert item[0]["name"] == "PC1"


def test_create(client_fixture: TestClient):
    response = client_fixture.post("/items", json={"name": "スマホ", "price": 30000, "user_id": 1})
    assert response.status_code == 201
    item = response.json()
    assert item["id"] == 3
    assert item["name"] == "スマホ"
    assert item["price"] == 30000

    response = client_fixture.post("/items")
    assert len(response.json()) == 3
    



    