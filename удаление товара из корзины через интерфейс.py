@allure.feature("Корзина")
@allure.story("Удаление товара через UI")
@pytest.mark.ui
def test_remove_from_cart_ui():
    driver = webdriver.Chrome()
    driver.get("https://pizzaroni.ru")
    with allure.step("Добавить товар в корзину"):
        driver.find_element(By.XPATH, "//button[contains(text(), 'Добавить в корзину')]").click()
    with allure.step("Удалить товар"):
        driver.find_element(By.ID, "cart-button").click()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Удалить')]").click()
        assert "Корзина пуста" in driver.page_source
    driver.quit()
