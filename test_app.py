import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_add_movie_page(client):
    response = client.get('/users/1/add_movie')
    assert response.status_code != 404, "Route /add_movie not found"
    assert response.status_code == 200
    assert b'Add Movie' in response.data

def test_update_movie_page(client):
    response = client.get('/users/1/update_movie/1')
    assert response.status_code == 200
    assert b'Update Movie' in response.data

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to MovieWeb App!' in response.data

def test_404_error(client):
    response = client.get('/non_existent_page')
    assert response.status_code == 404
    assert b'Page Not Found' in response.data

