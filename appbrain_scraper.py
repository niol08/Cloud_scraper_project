from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.appbrain.com/apps/trending/no-ads"
SCROLL_PAUSE_TIME = 1
SCRAPING_DURATION = 300  # 5 minutes

def scrape_app_names():
    """Scrape app names from AppBrain and return as a list."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get(URL)
    start_time = time.time()
    last_height = driver.execute_script("return document.body.scrollHeight")

    app_names = set()

    while time.time() - start_time < SCRAPING_DURATION:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

        elements = driver.find_elements(By.CSS_SELECTOR, "div.browse-app-large-title")
        for e in elements:
            name = e.text.strip()
            if name:
                app_names.add(name)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    driver.quit()
    return list(app_names)
