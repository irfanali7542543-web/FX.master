import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

# ویڈیوز کو ہمیشہ کے لیے محفوظ کرنے کا فولڈر
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# فرضی یا ڈیٹا بیس لسٹ (اس کو آپ ڈیٹا بیس سے بھی جوڑ سکتے ہیں)
posts = []

@app.route('/')
def index():
    # یہاں تمام پوسٹس ایک کے بعد ایک اوپر نیچے نظر آئیں گی
    return render_template('index.html', posts=posts)

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' in request.files:
        file = request.files['video']
        if file.filename != '':
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # ویڈیو کی معلومات لسٹ میں محفوظ کرنا تاکہ وہ ہمیشہ رہے
            posts.append({
                'username': 'FX_Master',
                'video_url': url_for('static', filename='uploads/' + file.filename),
                'caption': request.form.get('caption', 'New trading session #fx')
            })
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
