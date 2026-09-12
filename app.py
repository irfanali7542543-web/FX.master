from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# List to store uploaded videos in memory temporarily
videos_list = [
    {
        "id": 1,
        "caption": "FX Master Live Trade #trading #crypto",
        "url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "username": "@fx_trader"
    }
]

@app.route('/')
def home():
    return render_template('index.html', videos=videos_list)

@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        caption = request.form.get('caption', 'FX Master Video')
        # Add video to the feed list dynamically
        new_video = {
            "id": len(videos_list) + 1,
            "caption": caption,
            "url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "username": "@fx_trader"
        }
        videos_list.insert(0, new_video)
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
