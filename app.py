import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for videos
videos_db = [
    {
        "id": "1",
        "username": "@fx_master",
        "caption": "FX Master Video #trending",
        "url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "likes": 120,
        "comments": 45,
        "reposts": 12,
        "saved": 30
    }
]

@app.route('/')
def index():
    return render_template('index.html', videos=videos_db)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        caption = request.form.get('caption', 'FX Master Video #trending')
        video_url = request.form.get('videoUrl')
        
        if video_url:
            new_video = {
                "id": str(len(videos_db) + 1),
                "username": "@fx_user",
                "caption": caption,
                "url": video_url,
                "likes": 15,
                "comments": 4,
                "reposts": 1,
                "saved": 2
            }
            videos_db.insert(0, new_video)
            return redirect(url_for('index'))
            
    return render_template('upload.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
