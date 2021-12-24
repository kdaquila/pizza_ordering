import requests
from pizza_ordering import config


def test_find_pizza():
    response = requests.get(url=f"{config.back_end_url}/api/pizza")
    assert response.ok
    response_content = response.json()
    assert response_content["status"] == "success"
