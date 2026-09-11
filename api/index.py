import os
from flask import Flask, render_template

base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(os.path.dirname(base_dir), 'templates')
static_dir = os.path.join(os.path.dirname(base_dir), 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    return render_template('upload.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')
