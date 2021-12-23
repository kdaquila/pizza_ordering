import requests
from pizza_ordering import config


def test_order_pizza():
    # Action
    response = requests.post(url=f"{config.back_end_url}/api/pizza", json={"pizza_type": "cheese"})

    # Assert
    assert response.ok
    response_content = response.json()
    assert response_content["status"] == "success"
    assert response_content["data"]["pizza_id"] is not None
