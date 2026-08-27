from app import db, Signal, app
from datetime import datetime

def add_signal_to_db(pair, entry, tp, sl):
    with app.app_context():
        new_signal = Signal(pair=pair, entry=entry, take_profit=tp, stop_loss=sl)
        db.session.add(new_signal)
        db.session.commit()
        print(f"Signal for {pair} saved to Database successfully!")


if __name__ == "__main__":
    add_signal_to_db("BTC/USD", 65000.0, 67000.0, 64000.0)

