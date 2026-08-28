from flask import Flask, render_template, request, redirect, url_for, jsonify
from supabase import create_client, Client

app = Flask(__name__)

# Supabase Credentials
SUPABASE_URL = "https://dnarnrqlmrexrpnmdinx.supabase.co"
SUPABASE_KEY = "sb_publishable_Vp7kq-sNHQxL3E4MDmHFcw_HZ-p-fG1"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    try:
        response = supabase.table('videos').select('*').order('created_at', desc=True).execute()
        posts = response.data
    except Exception as e:
        posts = []
    return render_template('index.html', posts=posts)

@app.route('/upload', methods=['POST'])
def upload():
    video_url = request.form.get('video_url')
    if video_url:
        try:
            supabase.table('videos').insert({
                "video_url": video_url,
                "username": "forex_trader",
                "caption": "FX Master Trading Video"
            }).execute()
        except Exception as e:
            print("Error inserting to DB:", e)
    return redirect(url_for('index'))

@app.route('/api/videos', methods=['GET'])
def get_videos():
    try:
        response = supabase.table('videos').select('*').order('created_at', desc=True).execute()
        return jsonify({"success": True, "videos": response.data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/videos/<video_id>/like', methods=['POST'])
def like_video(video_id):
    try:
        return jsonify({"success": True, "message": "Like updated"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
