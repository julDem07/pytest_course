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

def test_logout(autologin):

    burger_menu = autologin.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    logout = autologin.find_element(By.CSS_SELECTOR,'#logout_sidebar_link').click()
    url_after = autologin.current_url

    assert url_after == "https://www.saucedemo.com/"