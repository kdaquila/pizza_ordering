import requests
from pizza_ordering import config

def test_cancel_valid_pizza():
    # Arrange
    create_pizza_response = requests.post(url=f"{config.back_end_url}/api/pizza", json={"pizza_type":"cheese"})
    new_pizza_id = create_pizza_response.json()["data"]["pizza_id"]
    cancel_pizza_response = requests.put(url=f"{config.back_end_url}/api/pizza/{new_pizza_id}")
    assert cancel_pizza_response.ok
    response_content = cancel_pizza_response.json()
    assert response_content["status"] == "success"

def test_cancel_invalid_pizza():
    # Arrange
    cancel_pizza_response = requests.put(url=f"{config.back_end_url}/api/pizza/100")
    assert cancel_pizza_response.ok
    response_content = cancel_pizza_response.json()
    assert response_content["status"] == "fail"
