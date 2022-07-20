import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_pypi():
    Driver=webdriver.Chrome(ChromeDriverManager().install())
    Driver.get("https://py.org/")
    Driver.maximize_window()
    Driver.find_element(By.XPATH,"(//a[text()='Log in'])[position()=1]").click()
    Driver.find_element(By.NAME,"username").send_keys("murlijha23")
    Driver.find_element(By.NAME,"password").send_keys("Testing@4321")
    Driver.find_element(By.XPATH,"//input[@type='submit']").click()
    print("login has been successfully completed")
    time.sleep(7)
    Driver.close()
