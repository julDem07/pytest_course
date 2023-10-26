import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def chrome_driver():
    driver = webdriver.Chrome()
    # driver.get("https://www.google.com/")
    yield driver
    driver.close()

@pytest.fixture()
def autologin(chrome_driver):
    chrome_driver.get("https://www.saucedemo.com/")

    chrome_driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")

    chrome_driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")

    chrome_driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    yield chrome_driver

def test_add_item_in_card(autologin):

    text_before = autologin.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name ']").text
    print(text_before)

    button_add = autologin.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    button_add.click()
    time.sleep(2)

    card = autologin.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    card.click()
    time.sleep(2)

    text_after = autologin.find_element(By.CSS_SELECTOR,
                                         "a[id='item_4_title_link'] > div[class='inventory_item_name']").text
    assert text_before == text_after
