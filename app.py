@app.route('/upload', methods=['POST'])
def upload():
    video_url = request.form.get('video_url')
    # Agar direct file upload ho rahi hai ya URL aa raha hai dono ko handle karein
    if 'video_file' in request.files:
        file = request.files['video_file']
        if file.filename != '':
            # Filename ko save ya URL mein convert karne ka logic
            video_url = f"/static/uploads/{file.filename}"
            file.save(os.path.join('static/uploads', file.filename))
            
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
