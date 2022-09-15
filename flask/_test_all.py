import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_home_bad_http_method(client):
    resp = client.post('/')
    assert resp.status_code == 405