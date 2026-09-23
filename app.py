from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/channel')
def channel():
    return render_template('channel.html')

@app.route('/for-you')
def for_you():
    return render_template('new_features/for_you.html')

@app.route('/inbox')
def inbox():
    return render_template('new_features/inbox.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
