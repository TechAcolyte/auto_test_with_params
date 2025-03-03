import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_add_to_backet(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
