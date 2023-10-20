import argparse
import os
from moviepy.editor import VideoFileClip

# Создание парсера аргументов командной строки
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Путь к файлу')

# Парсинг аргументов командной строки
args = parser.parse_args()

# Получение значения аргумента --input
user_input = args.input
print("user_input", user_input)

class VideoConverter:
    def __init__(self, video_files):
        self.video_files = video_files
        print("self.video_files", video_files)

    def convert_to_mp4(self):
        self.extract_audio(user_input)
        print("extract_audio", user_input)
            
    def extract_audio(self, video_file):
        clip = VideoFileClip(video_file)
        video_filename = os.path.splitext(video_file)[0] + '_' + '.mp4'
        clip.write_videofile(video_filename, codec='mpeg4')
        clip.close()
        print(f"Видео сконвертировано из {video_file} и сохранено в {video_filename}")

# Создание экземпляра класса VideoConverter и передача файла
converter = VideoConverter([user_input])
converter.convert_to_mp4()
