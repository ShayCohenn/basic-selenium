from selenium import webdriver
from selenium.webdriver.common.by import By

def main() -> None:
    """Prints the total number of articles from Wikipedia English."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://en.wikipedia.org/wiki/Main_Page")

    total_articles: str = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text

    print(total_articles)

if __name__ == '__main__':
    main()