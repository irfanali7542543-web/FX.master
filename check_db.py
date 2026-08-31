from supabase import create_client, Client

SUPABASE_URL = "https://dnarnrqlmrexrpnmdinx.supabase.co"
SUPABASE_KEY = "sb_publishable_Vp7kq-sNHQxL3E4MDmHFcw_HZ-p-fG1"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

try:
    # Test fetching data from videos table
    response = supabase.table('videos').select('*').execute()
    print("SUCCESS: Connected to Supabase! Data found:", response.data)
except Exception as e:
    print("ERROR: Could not fetch from 'videos' table. Error details:", e)
