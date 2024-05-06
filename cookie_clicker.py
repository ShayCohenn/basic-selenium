from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

def main() -> None:
    """Cheat in cookie clicker game"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://orteil.dashnet.org/cookieclicker/")

    time.sleep(4)

    english_button: WebElement = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
    english_button.click()

    time.sleep(4)

    cookie_button: WebElement = driver.find_element(By.XPATH, value='//*[@id="bigCookie"]')

    while True:
        cookie_button.click()
    
if __name__ == "__main__":
    main()