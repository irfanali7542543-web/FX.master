from supabase import create_client

# یہاں اپنے Supabase کے لنکس ڈالیں
url = "https://dnarnrqlmrexrpnmdinx.supabase.co"
key = "sb_publishable_Vp7kq-sNHQxL3E4MDmHFcw_HZ-p-fG1"
supabase = create_client(url, key)

# سگنل ڈیٹا یہاں ڈالیں
def add_signal(symbol, entry, signal_type, status):
    data = supabase.table("signals").insert({
        "symbol": symbol,
        "entry_price": entry,
        "signal_type": signal_type,
        "status": status
    }).execute()
    print("ڈیٹا Supabase میں محفوظ ہو گیا!")

# مثال: سگنل چلانے کے لیے یہ لائن استعمال کریں
add_signal("XAUUSD", 2400.50, "BUY", "ACTIVE")
