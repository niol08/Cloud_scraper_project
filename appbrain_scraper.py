from playwright.sync_api import sync_playwright
import time

APPBRAIN_URL = "https://www.appbrain.com/apps/trending/no-ads"
SCRAPING_DURATION = 300  # seconds
SCROLL_PAUSE_TIME = 1


def scrape_app_names():
    app_names = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        print("[STEP 1] Navigating to AppBrain...")
        page.goto(APPBRAIN_URL)

        start_time = time.time()
        last_height = page.evaluate("document.body.scrollHeight")

        while time.time() - start_time < SCRAPING_DURATION:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(SCROLL_PAUSE_TIME)

            titles = page.locator("div.browse-app-large-title").all_text_contents()
            app_names.update([title.strip() for title in titles if title.strip()])

            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        browser.close()

    print(f"[DONE] Scraped {len(app_names)} app names.")
    return list(app_names)
