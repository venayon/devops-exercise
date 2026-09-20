import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_get_items():
    client = app.test_client()

    response = client.get("/api/items")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_create_item():
    client = app.test_client()

    response = client.post(
        "/api/items",
        json={"name": "Terraform"},
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["name"] == "Terraform"
    assert "id" in data


def test_create_item_without_name():
    client = app.test_client()

    response = client.post(
        "/api/items",
        json={},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "name is required"}