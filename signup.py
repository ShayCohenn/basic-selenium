from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time

def main() -> None:
    """Signs up to a test website."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://secure-retreat-92358.herokuapp.com/")

    first_name_element: WebElement = driver.find_element(By.NAME, value="fName")
    last_name_element: WebElement = driver.find_element(By.NAME, value="lName")
    email_element: WebElement = driver.find_element(By.NAME, value="email")
    button_element: WebElement = driver.find_element(By.XPATH, value='/html/body/form/button')

    first_name_element.send_keys("first")
    time.sleep(1)
    last_name_element.send_keys("last")
    time.sleep(1)
    email_element.send_keys("email@gmail.com")
    time.sleep(1)
    button_element.click()

if __name__ == "__main__":
    main()