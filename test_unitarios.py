from fastapi.testclient import TestClient
from main import app  # Asegúrate de que importas correctamente tu instancia FastAPI
import pytest

# Crea una instancia de la aplicación FastAPI
client = TestClient(app, base_url="http://localhost:8000")
# Test para el endpoint raíz
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "¡Bienvenido a la API de Artesanos!"}

# Test para listar todos los artesanos
def test_get_artesanos():
    response = client.get("/api/artesanos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Se asegura que haya artesanos
    
def test_get_productos_by_artesano():
    response = client.get("/api/productos/artesano/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

# Test para obtener productos
def test_get_productos():
    response = client.get("/api/productos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0




