import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """Flask app test fixture"""
    return flask_app

@pytest.fixture
def client(app):
    """Flask test client"""
    return app.test_client()

def test_index_route(client):
    """Root path test"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data