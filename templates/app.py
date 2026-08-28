import os
from flask import Flask, render_template, request, redirect, url_for
from supabase import create_client, Client

app = Flask(__name__)

SUPABASE_URL = "https://dnarnrqlmrexrpnmdinx.supabase.co"
SUPABASE_KEY = "sb_publishable_Vp7kq-sNHQxL3E4MDmHFcw_HZ-p-fG1"
SUPABASE_BUCKET = "video"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' in request.files:
        file = request.files['video']
        if file.filename != '':
            try:
                file_bytes = file.read()
                file_path = f"uploads/{file.filename}"
                
                # Supabase میں ڈائریکٹ اپ لوڈ
                res = supabase.storage.from_(SUPABASE_BUCKET).upload(
                    path=file_path,
                    file=file_bytes,
                    file_options={"content-type": file.content_type}
                )
                
                public_url = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(file_path)
                
                posts.insert(0, {
                    'username': 'FX_Master',
                    'video_url': public_url,
                    'caption': request.form.get('caption', 'New trading session #fx')
                })
            except Exception as e:
                print("Error uploading to Supabase:", e)
                
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
