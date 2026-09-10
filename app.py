from flask import Flask, render_template, request, redirect, url_for, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# Yahan apni asli Supabase URL aur Key dal dein
SUPABASE_URL = "https://dnarnrqlmrexrpnmdinx.supabase.co"
SUPABASE_KEY = "sb_publishable_Vp7kq-sNHQxL3E4MDmHFcw_HZ-p-fG1"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    try:
        response = supabase.table('videos').select("*").order('id', desc=True).execute()
        videos_list = response.data if response.data else []
    except Exception as e:
        videos_list = []
    
    return render_template('index.html', videos=videos_list)

@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        if 'video' not in request.files:
            return jsonify({'success': False, 'error': 'No video file'})
            
        video_file = request.files['video']
        caption = request.form.get('caption', 'FX Master Signal')
        username = request.form.get('username', 'fx_trader')

        if video_file.filename == '':
            return jsonify({'success': False, 'error': 'Empty filename'})

        try:
            file_path = f"public/{video_file.filename}"
            file_bytes = video_file.read()
            
            supabase.storage.from_('videos_bucket').upload(
                path=file_path,
                file=file_bytes,
                file_options={"content-type": "video/mp4"}
            )
            
            video_url = supabase.storage.from_('videos_bucket').get_public_url(file_path)
            
            supabase.table('videos').insert({
                "url": video_url,
                "caption": caption,
                "username": username
            }).execute()

            return jsonify({'success': True, 'message': 'Video uploaded successfully'})
            
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'success': False, 'error': str(e)})
            
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
