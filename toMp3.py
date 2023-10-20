import argparse, os
from moviepy.editor import VideoFileClip

# Создание парсера аргументов командной строки
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Путь к файлу или список файлов')

# Парсинг аргументов командной строки
args = parser.parse_args()

# Получение значения аргумента --input
user_input = args.input

# Продолжение кода класса VideoToMP3Converter
class VideoToMP3Converter:
    def __init__(self, video_files):
        self.video_files = video_files

    def convert_files(self):
        for video_file in self.video_files:
            self.extract_audio(video_file)

    def extract_audio(self, video_file):
        clip = VideoFileClip(video_file)
        audio_filename = os.path.splitext(video_file)[0] + '.mp3'
        clip.audio.write_audiofile(audio_filename)
        clip.close()
        print(f"Аудио извлечено из {video_file} и сохранено в {audio_filename}")

# Создание экземпляра класса VideoToMP3Converter и передача списка файлов
converter = VideoToMP3Converter(user_input.split())

# Выполнение конвертации файлов
converter.convert_files()

# input("2 Нажмите Enter для выхода...") 
