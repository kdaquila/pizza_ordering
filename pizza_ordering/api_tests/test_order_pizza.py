import requests
from pizza_ordering import config


def test_order_pizza():
    response = requests.post(url=f"{config.back_end_url}/api/pizza", json={"pizza_type": "cheese"})
    assert response.ok
    response_content = response.json()
    assert response_content["status"] == "success"
