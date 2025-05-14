from appbrain_scraper import scrape_app_names
from playstore_email_scraper import collect_emails

def main():
    print("[STEP 1] Scraping AppBrain app names...")
    app_names = scrape_app_names()
    print(f"[DONE] Scraped {len(app_names)} app names.")

    print("[STEP 2] Collecting developer emails from Play Store...")
    emails = collect_emails(app_names)
    print(f"[DONE] Collected {len(emails)} new emails.")

if __name__ == "__main__":
    main()
