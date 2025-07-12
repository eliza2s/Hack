import sys
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips

def main(input_path, output_path):
    # --- Your detection logic here ---
    # For demo, let's just take the first 10 seconds as a highlight
    video = VideoFileClip(input_path)
    highlight = video.subclip(0, min(10, video.duration))
    highlight.write_videofile(output_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python highlight_script.py input.mp4 output.mp4")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])