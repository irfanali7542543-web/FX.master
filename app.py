from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')

@app.route('/friends')
def friends():
    return render_template('index.html') # Filhaal home page dikhayega taki 404 na aaye

@app.route('/inbox')
def inbox():
    return render_template('index.html') # Filhaal home page dikhayega taki 404 na aaye

if __name__ == '__main__':
    app.run(debug=True)
