from supabase import create_client, Client

SUPABASE_URL = "https://dnarnrqlmrexrpnmdinx.supabase.co"
SUPABASE_KEY = "sb_publishable_Vp7kq-sNHQxL3E4MDmHFcw_HZ-p-fG1"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# SQL query to create the videos table via Supabase RPC or direct insert test
try:
    # Let's insert a dummy row to see if it auto-creates or if we can initialize
    response = supabase.table('videos').insert({
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "username": "fx_master",
        "caption": "Test Video"
    }).execute()
    print("SUCCESS: Table created and test video inserted!", response.data)
except Exception as e:
    print("NOTE/ERROR:", e)
