from flask import Flask, render_template, request, redirect, url_for
import os
import time

app = Flask(__name__)

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

videos = ['fx_video.mp4']
comments_db = {
    'fx_video.mp4': [
        {"user": "Shabbir Numberdar", "text": "ya Allah", "time": "1h"},
        {"user": "alisha", "text": "stand with Palestine", "time": "1h"}
    ]
}

@app.route('/')
def home():
    idx = int(request.args.get('v', 0))
    if idx >= len(videos) or idx < 0:
        idx = 0
    current_vid = videos[idx]
    vid_comments = comments_db.get(current_vid, [])
    return render_template('battle.html', current_video=current_vid, comments=vid_comments, current_index=idx, total_videos=len(videos))

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' in request.files:
        file = request.files['video']
        if file.filename != '':
            filename = f"video_{int(time.time())}.mp4"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            videos.append(filename)
            comments_db[filename] = [{"user": "FX Master", "text": "New video uploaded!"}]
    return redirect(url_for('home', v=len(videos)-1))

@app.route('/add_comment', methods=['POST'])
def add_comment():
    vid = request.form.get('video_name')
    comment_text = request.form.get('comment_text')
    if vid in comments_db and comment_text:
        comments_db[vid].insert(0, {"user": "You", "text": comment_text, "time": "Just now"})
    vid_idx = videos.index(vid) if vid in videos else 0
    return redirect(url_for('home', v=vid_idx))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
