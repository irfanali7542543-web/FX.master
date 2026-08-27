from pymongo import MongoClient

# MongoDB Atlas Connection
connection_string = "YOUR_CONNECTION_STRING_HERE"
client = MongoClient(connection_string)

# Database and Collection setup
db = client['fx_mastar_db']
signals = db['signals_collection']

# Function to save data
def save_signal(signal_data):
    try:
        signals.insert_one(signal_data)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
