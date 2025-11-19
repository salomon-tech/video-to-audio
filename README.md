🎵 Video-to-Audio Converter (Python)

A simple Python script that converts any video file into an audio file (MP3) using MoviePy.

This tool is perfect for quickly extracting soundtracks, music, interviews, or voice notes from any video format.

🚀 Features

Convert any video to MP3

Lightweight and easy to use

Powered by MoviePy

📦 Requirements

Install MoviePy:

pip install moviepy

▶️ Usage

Place your video in the same folder as the script, then run:

python main.py

You can customize the input and output file names inside the script:

video_path = "converted_vedeo.mp4"
audio_path = "converter_audio.mp3"

🧩 Code Overview

The script:

Loads the video file

Extracts the audio track

Saves it as an MP3

Closes all resources

📄 Notes

Supported input formats: .mp4, .mov, .avi, .mkv, etc.

Output format: .mp3

Make sure the file paths are correct before running the script.
