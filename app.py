from flask import Flask, render_template, request, redirect, url_for
import base64

app = Flask(__name__)

videos_db = [
    {
        "id": 1,
        "caption": "FX Master Live Trade #trading #crypto",
        "url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "username": "@fx_trader",
        "likes": 942,
        "comments": 45,
        "saved": 33
    }
]

@app.route('/')
def home():
    return render_template('index.html', videos=videos_db)

@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        caption = request.form.get('caption', 'FX Master Video')
        file = request.files.get('video_file')
        
        try:
            if file and file.filename != '':
                file_bytes = file.read()
                # Limit size check for Vercel stability
                if len(file_bytes) < 4500000:
                    encoded_video = base64.b64encode(file_bytes).decode('utf-8')
                    video_url = f"data:video/mp4;base64,{encoded_video}"
                else:
                    video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
            else:
                video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
        except Exception:
            video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
        
        new_video = {
            "id": len(videos_db) + 1,
            "caption": caption,
            "url": video_url,
            "username": "@fx_user",
            "likes": 15,
            "comments": 3,
            "saved": 2
        }
        videos_db.insert(0, new_video)
        return redirect(url_for('home'))
        
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

if __name__ == '__main__':
    app.run(debug=True)
