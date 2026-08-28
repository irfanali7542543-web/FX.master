import os
from flask import Flask, render_template, request, redirect, url_for, flash
from supabase import create_client, Client

app = Flask(__name__)
app.secret_key = 'fx_master_secret_key'

# Yahan apni Supabase ki asli URL aur Anon Key lagayein (jo aapke Supabase account mein hain)
SUPABASE_URL = "https://dnarnrqlmrexrpnmdinx.supabase.co"
SUPABASE_KEY = "sb_publishable_Vp7kq-sNHQxL3E4MDmHFcw_HZ-p-fG1"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    try:
        # Supabase database se videos fetch karna
        response = supabase.table("videos").select("*").execute()
        videos = response.data if response.data else []
    except Exception as e:
        videos = []
    return render_template('index.html', videos=videos)

@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        if 'video' not in request.files:
            flash('Koi video file select nahi ki gayi!')
            return redirect(request.url)
        
        file = request.files['video']
        caption = request.form.get('caption', 'FX Master Trade')
        
        if file.filename == '':
            flash('File ka naam khali hai')
            return redirect(request.url)
            
        try:
            file_bytes = file.read()
            file_name = f"uploads/{os.urandom(8).hex()}_{file.filename}"
            
            # Supabase Storage mein video upload karna (ensure karein ke 'videos-bucket' naam ka bucket bana ho)
            supabase.storage.from_("videos-bucket").upload(file_name, file_bytes, {"file": file.mimetype})
            
            # Public URL lena
            public_url = supabase.storage.from_("videos-bucket").get_public_url(file_name)
            
            # Supabase database mein record save karna
            supabase.table("videos").insert({"url": public_url, "caption": caption}).execute()
            
            return redirect(url_for('home'))
        except Exception as e:
            flash(f"Upload fail ho gaya: {str(e)}")
            return redirect(request.url)
            
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
