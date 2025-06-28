from flask import Flask, request, jsonify, send_file
import subprocess
import uuid
import os

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data.get("text")
    if not text:
        return jsonify({"error": "Text required"}), 400

    uid = str(uuid.uuid4())
    out_path = f"temp/{uid}.wav"
    os.makedirs("temp", exist_ok=True)

    try:
        subprocess.run([
            "tts", "--text", text, "--out_path", out_path
        ], check=True)

        return send_file(out_path, mimetype="audio/wav")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def health():
    return "🟢 Coqui TTS API is live"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
