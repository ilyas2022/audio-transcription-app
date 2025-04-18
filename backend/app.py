import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """Flask 앱 테스트 픽스처"""
    return flask_app

@pytest.fixture
def client(app):
    """Flask 테스트 클라이언트"""
    return app.test_client()

def test_index_route(client):
    """루트 경로 테스트"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_websocket_echo():
    """웹소켓 에코 기능 테스트 (간단한 골격만 제공)"""
    # 실제 웹소켓 테스트는 별도의 라이브러리나 방법이 필요할 수 있음
    # 여기서는 placeholder로 넣어둠
    assert True