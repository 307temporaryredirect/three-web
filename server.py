from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Load data dari JSON hasil generate_description.py
with open('zodiac_mbti_descriptions.json', 'r', encoding='utf-8') as f:
    descriptions = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_description')
def get_description():
    zodiac = request.args.get('zodiac')
    mbti = request.args.get('mbti')
    key = f"{zodiac}-{mbti}"
    description = descriptions.get(key, "Deskripsi untuk kombinasi ini belum tersedia. Silakan coba kombinasi lain atau tunggu update dari kami.")
    return jsonify({'description': description})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
