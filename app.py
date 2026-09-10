import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Default sample video jab tak koi apni video upload na kare
current_video_path = "https://www.w3schools.com/html/mov_bbb.mp4"

@app.route('/')
def home():
    return render_template('battle.html', current_video=current_video_path)

@app.route('/upload', methods=['POST'])
def upload_video():
    global current_video_path
    if 'videoFile' in request.files:
        file = request.files['videoFile']
        if file.filename != '':
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            # Set the path to the newly uploaded video in static folder
            current_video_path = url_for('static', filename=f'uploads/{filename}')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
