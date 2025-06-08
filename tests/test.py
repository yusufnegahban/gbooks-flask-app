import pytest
from app import create_app

# This fixture creates a test client for the Flask app
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True  # Enables testing mode
    client = app.test_client()    # Creates a test client
    return client

# Test the home page ("/") to ensure it loads successfully
def test_home_page(client):
    response = client.get('/')  # Sends a GET request to the home page
    assert response.status_code == 200  # Check if status code is OK
    assert b"Book" in response.data  # Check if the word "Book" is in the response (update based on your actual page content)
