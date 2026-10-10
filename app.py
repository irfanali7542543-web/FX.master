import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({"status": "running", "message": "FX Master backend is live on Vercel!"})

if __name__ == '__main__':
    app.run(debug=True)
