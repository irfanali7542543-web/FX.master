from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/for-you')
def for_you():
    return render_template('for_you.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/channel')
def channel():
    return render_template('channel.html')

if __name__ == '__main__':
    app.run(debug=True)
