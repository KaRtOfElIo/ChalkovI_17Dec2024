@allure.feature("Корзина")
@allure.story("Изменение количества товара")
@pytest.mark.api
def test_update_cart_quantity():
    payload = {"product_id": 1, "quantity": 1}
    requests.post(f"{BASE_URL}/cart/add", json=payload)  # Добавляем товар
    update_payload = {"product_id": 1, "quantity": 2}
    response = requests.put(f"{BASE_URL}/cart/update", json=update_payload)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["cart"]["items"][0]["quantity"] == 2
