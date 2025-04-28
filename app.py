from flask import Flask, request, jsonify
import os
import random
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Example trending hashtags
TRENDING_HASHTAGS = [
    "#love", "#instagood", "#photooftheday", "#fashion", "#beautiful",
    "#happy", "#cute", "#tbt", "#like4like", "#followme",
    "#picoftheday", "#follow", "#me", "#selfie", "#summer",
    "#art", "#instadaily", "#friends", "#repost", "#nature"
]

# Example captions
SUGGESTED_CAPTIONS = [
    "Living my best life ✨",
    "Sunshine mixed with a little hurricane ☀️🌪️",
    "Collecting memories, not things 📸",
    "Stay strong, the weekend is coming 💪",
    "Dream big, sparkle more, shine bright 💫"
]

# Example best times
BEST_TIMES = [
    "8 AM - 10 AM",
    "12 PM - 2 PM",
    "6 PM - 9 PM",
    "7 PM - 9 PM",
    "5 PM - 7 PM"
]

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Mock processing: Randomly generate analysis result
    best_time = random.choice(BEST_TIMES)
    caption = random.choice(SUGGESTED_CAPTIONS)
    hashtags = random.sample(TRENDING_HASHTAGS, 5)

    response = {
        'status': 'success',
        'message': 'File uploaded and analyzed successfully!',
        'best_time': best_time,
        'caption': caption,
        'hashtags': hashtags
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
