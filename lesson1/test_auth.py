import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

@pytest.fixture(scope="module")
def chrome_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    yield driver
    driver.close()



def test_login_form(chrome_driver):
    chrome_driver.get("https://www.saucedemo.com/")

    username_field = chrome_driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = chrome_driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome_driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    assert chrome_driver.current_url == "https://www.saucedemo.com/inventory.html"

    time.sleep(3)

def test_incorrect_data(chrome_driver):
    chrome_driver.get("https://www.saucedemo.com/")

    username_field = chrome_driver.find_element(By.XPATH, "//input[@data-test='username']")
    username_field.send_keys("user")

    password_field = chrome_driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("eser")

    login_button = chrome_driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    expect_result = chrome_driver.find_element(By.XPATH, "//h3[@data-test='error']")

    assert expect_result.is_displayed()
    time.sleep(3)


@pytest.fixture()
def autologin(chrome_driver):
    chrome_driver.get("https://www.saucedemo.com/")

    username_field = chrome_driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = chrome_driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome_driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    yield chrome_driver

def test_login_with_fixture(autologin):
    assert autologin.current_url == "https://www.saucedemo.com/inventory.html"
    time.sleep(3)













