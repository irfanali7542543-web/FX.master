#!/bin/bash
# Terminal se video post karne ka command
# Use:./post_video.sh myvideo.mp4 "My caption"

VIDEO_PATH=$1
CAPTION=$2

if [ -z "$VIDEO_PATH" ]; then
  echo "Bhai video ka naam do! Example:./post_video.sh video.mp4"
  exit 1
fi

echo "Uploading $VIDEO_PATH to Supabase..."
# Supabase upload via curl
FILENAME=$(date +%s)_$(basename "$VIDEO_PATH")
curl -X POST "https://dnarnrqlmrexrpnmdinx.supabase.co/storage/v1/object/videos/$FILENAME" \
-H "apikey: sb_publishable_Vp7kq-sNHQX3E4MDmHFcw_HZ-p-fG1" \
-H "Authorization: Bearer sb_publishable_Vp7kq-sNHQX3E4MDmHFcw_HZ-p-fG1" \
-H "Content-Type: video/mp4" \
--data-binary @"$VIDEO_PATH"

echo ""
echo "Git pe push kar raha hu..."
git add.
git commit -m "Added video: $FILENAME - $CAPTION"
git push origin main
echo "Ho gaya bhai! Video live hai."
