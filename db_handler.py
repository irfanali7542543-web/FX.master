import psycopg2

# Connecting to the PostgreSQL database
conn = psycopg2.connect(database="fx_master_db")
cur = conn.cursor()

# Function to save signals permanently in the database
def save_signal_to_db(signal_name, signal_data):
    # Executing the insert command
    cur.execute("INSERT INTO signals (name, data) VALUES (%s, %s)", (signal_name, signal_data))
    conn.commit()
    print("Signal has been saved permanently in the database!")

# Testing the database connection by saving a sample signal
save_signal_to_db("Test_Signal", "Buy Gold at 2400")
