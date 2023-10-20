import sys, os
import subprocess
import time
from moviepy.editor import VideoFileClip

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

if __name__ == "__main__":

    # Проверяем, были ли указаны файлы в аргументах командной строки
    if len(sys.argv) < 2:
        print("Вы не указали файлы для конвертации.")
        sys.exit()

    # Создаем экземпляр класса VideoToMP3Converter и передаем список файлов
    converter = VideoToMP3Converter(sys.argv[1:])

    # Выполняем конвертацию файлов
    converter.convert_files()

    # input("2 Нажмите Enter для выхода...")    
