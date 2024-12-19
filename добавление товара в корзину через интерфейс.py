from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure

@allure.feature("Корзина")
@allure.story("Добавление товара через UI")
@pytest.mark.ui
def test_add_to_cart_ui():
    driver = webdriver.Chrome()
    driver.get("https://pizzaroni.ru")
    with allure.step("Добавить товар в корзину"):
        driver.find_element(By.XPATH, "//button[contains(text(), 'Добавить в корзину')]").click()
    with allure.step("Открыть корзину"):
        driver.find_element(By.ID, "cart-button").click()
        assert "Ваш заказ" in driver.page_source
    driver.quit()
