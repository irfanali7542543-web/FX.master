import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from supabase import create_client, Client

app = Flask(__name__)

# Supabase configuration (Vercel environment variables se uthayega)
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")
SUPABASE_BUCKET = "videos"  # Aapka Supabase storage bucket naam

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL and SUPABASE_KEY else None

# In-memory database for videos
videos_db = [
    {
        "id": "1",
        "username": "@fx_master",
        "caption": "FX Master Comedy & Trading #trending",
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
        
        # Check if file was uploaded
        if 'videoFile' in request.files:
            file = request.files['videoFile']
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file_bytes = file.read()
                
                video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
                if supabase:
                    try:
                        # Upload file bytes to Supabase Storage bucket
                        supabase.storage.from_(SUPABASE_BUCKET).upload(
                            path=filename,
                            file=file_bytes,
                            file_options={"content-type": file.content_type, "upsert": "true"}
                        )
                        # Get Public URL
                        video_url = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(filename)
                    except Exception as e:
                        print("Supabase Upload Error:", e)
                
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
                
        # Check if direct URL was provided
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

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
