import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_email(email: str):
    """Insert a unique developer email to Supabase."""
    try:
        result = supabase.table("emails").insert({"email": email}).execute()
        if result.get("status_code") == 201:
            print(f"[✓] Saved: {email}")
        elif result.get("status_code") == 409 or (
            result.get("message") and "duplicate key value" in result["message"]
        ):
            print(f"[!] Duplicate: {email}")
        else:
            print(f"[ERROR] Failed to insert {email}: {result}")
    except Exception as e:
        print(f"[ERROR] Exception inserting {email}: {e}")

def fetch_emails():
    """Fetch all developer emails stored in Supabase."""
    return supabase.table("emails").select("*").execute()
