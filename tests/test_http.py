import pytest
import requests


@pytest.mark.http
def test_first_request():
    response = requests.get("https://api.github.com/zen")
    print(f"Response: {response.text}")


@pytest.mark.http
def test_second_request():
    response = requests.get("https://api.github.com/users/defunkt")
    json = response.json()
    
    assert json['name'] == "Chris Wanstrath"
    assert response.status_code == 200
    assert response.headers['Server'].lower() == "GitHub.com".lower()


@pytest.mark.http
def test_status_code_request():
    response = requests.get("https://api.github.com/users/sergii_butenko")
    assert response.status_code == 404