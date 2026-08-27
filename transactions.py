import datetime

def save_transaction(signal_data):
    try:
        with open("signals_history.txt", "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - {signal_data}\n")
        return True
    except Exception as e:
        return False
