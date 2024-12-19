import requests
import pytest
import allure

BASE_URL = "https://pizzaroni.ru/api"

@allure.feature("Корзина")
@allure.story("Добавление товара")
@pytest.mark.api
def test_add_to_cart():
    payload = {"product_id": 1, "quantity": 1}
    response = requests.post(f"{BASE_URL}/cart/add", json=payload)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["cart"]["items"][0]["product_id"] == 1
    assert response.json()["cart"]["items"][0]["quantity"] == 1
