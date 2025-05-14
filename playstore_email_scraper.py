from google_play_scraper import search, app
from supabase_client import insert_email

SEARCH_RESULTS_PER_QUERY = 50

def collect_emails(app_names):
    """Collect and insert developer emails for given app names."""
    collected = set()

    for term in app_names:
        try:
            results = search(term, lang='en', n_hits=SEARCH_RESULTS_PER_QUERY)
        except Exception as e:
            print(f"[!] Error searching '{term}': {e}")
            continue

        for app_summary in results:
            app_id = app_summary.get("appId")
            if not app_id:
                continue
            try:
                details = app(app_id)
                email = details.get("developerEmail")
                if email and email.endswith("@gmail.com") and email not in collected:
                    collected.add(email)
                    insert_email(email)
                    print(f"[✓] Saved: {email}")
            except Exception as e:
                print(f"[!] Error fetching app {app_id}: {e}")

    return collected
