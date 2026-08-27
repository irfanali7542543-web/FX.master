import os
import time

# Processes to monitor
processes = ["FX_Web", "Signals_Script"]

def check_status():
    for proc in processes:
        # Check the status of the process
        status = os.popen(f"pm2 describe {proc} --silent | grep 'status'").read()
        
        if "online" not in status:
            print(f"ALERT: {proc} is DOWN! Attempting to restart...")
            os.system(f"pm2 restart {proc}")
        else:
            print(f"System Check: {proc} is running perfectly.")

while True:
    check_status()
    # Wait for 60 seconds before next check
    time.sleep(60)
