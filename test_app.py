import pytest
import app

def test_home():
    with app.app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200, "სიმულირებული ჩავარდნა CI/CD პაიპლაინში"
