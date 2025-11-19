from moviepy.editor import VideoFileClip

def convert_video(video_path, audio_path):
    video_path = VideoFileClip(video_path)
    audio_path = video_path.audio
    audio_path.write_audiofile(audio_path)
    video_path.close()
    audio_path.close()

if __name__ == "__main__":
    video_path = "converted_vedeo.mp4"
    audio_path = "converter_audio.mp3"
    convert_video(video_path, audio_path)