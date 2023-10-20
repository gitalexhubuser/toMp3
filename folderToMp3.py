import argparse
import os
from moviepy.editor import VideoFileClip

# Создание парсера аргументов командной строки
parser = argparse.ArgumentParser()
parser.add_argument('folder_path', help='Путь к папке с видеофайлами')

# Парсинг аргументов командной строки
args = parser.parse_args()

# Получение пути к папке из аргументов командной строки
folder_path = args.folder_path

# Продолжение кода класса VideoToMP3Converter
class VideoToMP3Converter:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def convert_files(self):
        video_files = self.get_video_files()
        for video_file in video_files:
            self.extract_audio(video_file)

    def get_video_files(self):
        video_files = []
        for file_name in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file_name)
            if os.path.isfile(file_path) and file_name.lower().endswith('.mp4'):
                video_files.append(file_path)
        return video_files

    def extract_audio(self, video_file):
        clip = VideoFileClip(video_file)
        audio_filename = os.path.splitext(video_file)[0] + '.mp3'
        clip.audio.write_audiofile(audio_filename)
        clip.close()
        print(f"Аудио извлечено из {video_file} и сохранено в {audio_filename}")

# Создание экземпляра класса VideoToMP3Converter и передача пути к папке
converter = VideoToMP3Converter(folder_path)

# Выполнение конвертации файлов
converter.convert_files()