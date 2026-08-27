import time
from supabase import create_client

url = "https://dnarnrqlmrexrpnmdinx.supabase.co"
key = "sb_publishable_Vp7kq-sNHQxL3E4MDmHFcw_HZ-p-fG1"

supabase = create_client(url, key)

def check_server():
    try:
        # 1. Server check
        data = supabase.table("signals").select("*").limit(1).execute()
        print(f"[{time.ctime()}] Heartbeat: Server is healthy!")
        
        # 2. Yahan apna main kaam (signals bhejne wala logic) likhein
        # Jo har 5 ya 15 minute mein chalega
        
    except Exception as e:
        print(f"[{time.ctime()}] Alert: Error: {e}")

while True:
    check_server()
    # 300 seconds = 5 minute ka delay
    time.sleep(300) 
