from fastapi.testclient import TestClient
from jwt_auth_server.main import app

client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}


# Test 1: User can succesfully login
def test_login():
    pass


# Test 2: User gets 403 on invalid credentials
def test_bad_credentials():
    pass


# Test 3: User receives 401 on expired token
def test_expired_token():
    pass


# Test 4: User can refresh access token using refresh token
def test_refresh_access_token():
    pass


# Test 5: User can use refresh token only once
def test_refresh_token_used_once():
    pass


# Test 6: Refresh tokens become invalid on logout
def test_invalid_refresh_token_on_logout():
    pass


# Test 7: Multiple refresh tokens are valid
def test_multiple_refresh_tokens():
    pass
