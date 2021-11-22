from fastapi.testclient import TestClient
from jwt_auth_server.main import app

client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}
