from flask import Flask, request, send_file, jsonify
import os
import uuid
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def generate_highlight(input_path, output_path):
    """
    This function should run your detection and highlight creation logic.
    Replace the below example with your actual pipeline.
    """
    # Example: Call your highlight script with input and output paths
    # You can replace this with your own Python function if you want
    result = subprocess.run(
        ["python", "highlight_script.py", input_path, output_path],
        capture_output=True
    )
    return result.returncode == 0 and os.path.exists(output_path), result.stderr.decode()

@app.route("/api/highlight", methods=["POST"])
def highlight():
    if "video" not in request.files:
        return jsonify({"error": "No video uploaded"}), 400

    video = request.files["video"]
    video_id = str(uuid.uuid4())
    input_path = os.path.join(UPLOAD_FOLDER, f"{video_id}.mp4")
    output_path = os.path.join(OUTPUT_FOLDER, f"{video_id}_highlight.mp4")
    video.save(input_path)

    # Run highlight generation
    success, error = generate_highlight(input_path, output_path)
    if not success:
        return jsonify({"error": "Highlight generation failed", "details": error}), 500

    return send_file(output_path, as_attachment=True, download_name="highlight.mp4")

if __name__ == "__main__":
    app.run(debug=True)