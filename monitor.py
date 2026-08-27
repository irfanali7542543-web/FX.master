import os
from dotenv import load_dotenv

# .env فائل لوڈ کریں
load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# چیک کریں کہ کیا ٹوکن مل گیا ہے
if not TOKEN:
    print("Error: TOKEN not found in .env file")
else:
    print(f"Bot started with Token: {TOKEN[:10]}...") # صرف پہلا حصہ دکھائیں گے
    # یہاں آپ کا باقی کوڈ آئے گا...
