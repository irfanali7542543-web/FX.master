cat << 'EOF' > app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/group')
def group():
    return render_template('group.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
EOF
