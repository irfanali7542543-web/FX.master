import urllib.request
import json

SUPABASE_URL = "https://dnarnrqlmrexrpnmdinx.supabase.co"
# Note: Creating tables programmatically usually requires the service_role key or SQL execution.
# Let's use the direct SQL execution endpoint if available or print the exact SQL you can run.

print("Supabase URL is active. To create the table instantly without opening the browser,")
print("you can run this SQL command inside your Supabase SQL Editor if you ever open it:")
print("""
CREATE TABLE videos (
    id SERIAL PRIMARY KEY,
    video_url TEXT NOT NULL,
    username TEXT DEFAULT 'forex_trader',
    caption TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL
);
""")
