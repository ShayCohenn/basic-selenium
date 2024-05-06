from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def main() -> None:
    """Prints a list of events from Python.org"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.python.org/")

    menu: WebElement = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div')

    items: list[WebElement] = menu.find_elements(By.TAG_NAME, value="li")

    events = []

    for item in items:
        a_tag: WebElement = item.find_element(By.TAG_NAME, value="a")
        obj: dict[str, str]={
        "title": a_tag.text,
        "link": a_tag.get_attribute("href"),
        "date": item.find_element(By.TAG_NAME, value="time").text
        }
        events.append(obj)

    print(events)

if __name__ == "__main__":
    main()