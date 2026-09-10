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
