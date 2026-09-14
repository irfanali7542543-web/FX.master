from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

SUPABASE_URL = "https://dnarnrqlmrexrpnmdinx.supabase.co"
SUPABASE_KEY = "sb_publishable_Vp7kq-sNHQX3E4MDmHFcw_HZ-p-fG1"
BUCKET = "videos"

@app.route('/')
def index():
    try:
        headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
        res = requests.get(f"{SUPABASE_URL}/storage/v1/bucket/{BUCKET}/list", headers=headers)
        # public url se videos lena
        list_res = requests.post(f"{SUPABASE_URL}/storage/v1/object/list/{BUCKET}",
                                 headers=headers, json={"prefix": ""})
        videos = list_res.json() if list_res.status_code == 200 else []
        return render_template('index.html', videos=videos, supabase_url=SUPABASE_URL, bucket=BUCKET)
    except Exception as e:
        return render_template('index.html', videos=[], supabase_url=SUPABASE_URL, bucket=BUCKET)

@app.route('/upload')
def upload():
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
    app.run(debug=True)
