import subprocess
import os

while True:
    # Запрашиваем ввод от пользователя
    user_input = input("Перетащите видеофайл в эту консоль и нажмите Enter: ")

    # Проверка, что пользователь ввел путь к файлу
    if not user_input:
        print("Путь к файлу не был введен.")
        continue
    
    # Получение пути к файлу из переданного ввода пользователя
    file_path = user_input.strip()

    if user_input:
        # Получение пути к папке из переданного пути к файлу
        # folder_path = os.path.dirname(user_input)

        # Получение пути к папке из переданного пути к файлу
        folder_path = os.path.dirname(file_path)
        print("folder_path", folder_path)

        # Передача пути к папке в качестве аргумента команды
        command = ['python', 'folderToMp3.py', folder_path.strip('"')]
        subprocess.call(command, shell=True)