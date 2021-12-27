import requests
from pizza_ordering import config


def test_delete_pizza():
    requests.post(url=f"{config.back_end_url}/api/pizza", json={"pizza_type": "cheese"})
    response = requests.delete(url=f"{config.back_end_url}/api/pizza")
    assert response.ok
    response_content = response.json()
    assert response_content["status"] == "success"
