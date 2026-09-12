import os
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for serverless environment compatibility
videos_db = [
    {
        "id": 1,
        "caption": "FX Master Live Trade #trading #crypto",
        "url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "username": "@fx_trader"
    }
]

@app.route('/')
def home():
    return render_template('index.html', videos=videos_db)

@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        caption = request.form.get('caption', 'FX Master Trade')
        video_file = request.files.get('video')
        
        # For serverless, if a file is uploaded we can use a placeholder or handle blob storage
        # Here we add it to our list with a default sample or uploaded name
        new_video = {
            "id": len(videos_db) + 1,
            "caption": caption,
            "url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "username": "@fx_trader"
        }
        videos_db.insert(0, new_video)
        return redirect(url_for('home'))
        
    return render_template('upload.html')

@app.route('/api/videos', methods=['GET'])
def get_videos():
    return jsonify(videos_db)

@app.route('/inbox')
def inbox():
    return render_template('inbox.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
