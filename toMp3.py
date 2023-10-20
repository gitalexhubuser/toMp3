import sys
import shutil
from moviepy.editor import VideoFileClip

def extract_audio(video_file):
    try:
        clip = VideoFileClip(video_file)
        audio_filename = video_file.replace(video_file.split('.')[-1], 'mp3')
        clip.audio.write_audiofile(audio_filename)
        clip.close()
        print(f"Audio extracted from {video_file} to {audio_filename}")
    except:
        print(f"Failed to extract audio from {video_file}")

if __name__ == '__main__':
    
    for file in sys.argv[1:]:
        extract_audio(file)
