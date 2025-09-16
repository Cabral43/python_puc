from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root():
    """Testa se o endpoint principal ('/') retorna a saudação correta."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "Mundo"}


def test_read_item():
    """Testa se o endpoint de item retorna os dados corretos para um ID específico."""
    item_id = 5
    response = client.get(f"/items/{item_id}")

    assert response.status_code == 200
    assert response.json() == {
        "item_id": item_id,
        "name": f"Item {item_id}",
        "price": 10.0 * item_id
    }


def test_create_item():
    """Testa a criação de um novo item via POST."""
    item_data = {"name": "Meu Novo Item", "price": 99.90}

    response = client.post("/items/", json=item_data)

    assert response.status_code == 200
    expected_response = {
        "message": "Item criado com sucesso",
        "item": item_data
    }
    assert response.json() == expected_response