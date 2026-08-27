import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)

# Error Logging Configuration
if not app.debug:
    file_handler = RotatingFileHandler('core_files/error.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('FX Master Server Started')

@app.route('/')
def home():
    try:
        with open('signals_history.txt', 'r') as f:
            signals = f.readlines()[-5:]
    except:
        signals = ["No signals yet."]
    return render_template('index.html', signals=signals)

if __name__ == '__main__':
    app.run(debug=True)

