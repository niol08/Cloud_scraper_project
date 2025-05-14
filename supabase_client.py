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
        response = supabase.table("emails").upsert({"email": email}).execute()
        return response
    except Exception as e:
        print(f"[ERROR] Failed to insert {email}: {e}")
        return None

def fetch_emails():
    """Fetch all developer emails stored in Supabase."""
    return supabase.table("emails").select("*").execute()
