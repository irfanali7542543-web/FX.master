import urllib.request
import json

# آپ کے پروجیکٹ کی تفصیلات
SUPABASE_URL = "https://dnarnrqlmrexrpnmdinx.supabase.co"
SUPABASE_KEY = "sb_publishable_Vp7kq-sNHQxL3E4UDaHFcw_HZ-p-f61"

# نوٹ: Supabase کی پبلک کی سے ٹیبل بنانے کے لیے ہم پبلک اسکیما پر RPC یا PostgREST اینڈ پوائن트 استعمال کرتے ہیں۔
print("Checking connection to Supabase...")
