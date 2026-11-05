import os 

import pytest 

pytest.importorskip("selenium") 

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 

from testdata import STANDARD_USER 

BASE_URL = os.environ.get("TECHRETAIL_URL", "http://127.0.0.1:8000") 

def by_test(name): 
    return (By.CSS_SELECTOR, f"[data-test='{name}']") 
@pytest.fixture 
def driver(): 
    options = webdriver.ChromeOptions() 
    options.add_argument("--headless=new") 
    driver = webdriver.Chrome(options=options) 
    yield driver 
    driver.quit()

def test_selenium_fel_losenord_visar_felmeddelande(driver):
    # Arrange 
    driver.get(f"{BASE_URL}/logga-in") 
    # Act 
    driver.find_element(*by_test("email-input")).send_keys(STANDARD_USER.email) 
    driver.find_element(*by_test("password-input")).send_keys("fel-losenord") 
    driver.find_element(*by_test("login-button")).click() 
    # Assert 
    wait = WebDriverWait(driver, 5) 
    error = wait.until(EC.visibility_of_element_located(by_test("login-error"))) 
    assert error.text == "Fel e-post eller lösenord." 