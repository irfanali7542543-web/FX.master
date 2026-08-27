<<<<<<< HEAD
# --- Auto-Fix Database Initialization ---
from app import app, db

with app.app_context():
    db.create_all()
    print("Database tables verified and ready!")
# --- End of Auto-Fix ---
=======
import redis

# Connecting to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Function to save signal with a 10-minute expiry
def save_signal(signal_name, signal_data):
    # Data will automatically expire after 600 seconds
    r.setex(signal_name, 600, signal_data)
    print("Signal has been saved in cache successfully!")

# Function to get signal from cache
def get_signal(signal_name):
    data = r.get(signal_name)
    if data:
        return data.decode('utf-8')
    else:
        return "Signal has expired or not found in cache."

# Testing the signal storage
save_signal("test_signal", "Buy Gold at 2400")
print("Data sent to Redis!")
>>>>>>> 94212ba (FX-MASTAR initial push)
