import subprocess
import sys
import os
import time

if __name__ == "__main__":

    # Запоминание файлов, перетащенных на скрипт
    # Получение списка перетащенных файлов
    dropped_files = sys.argv[1:]
    print(dropped_files)

    # Проверка, что были перетащены файлы
    if len(dropped_files) == 0:
        print("Файлы не были перетащены на скрипт.")
        sys.exit(1)

    # Путь к исполняемому файлу командной строки (cmd.exe)
    cmd_path = r'C:\WINDOWS\system32\cmd.exe'  # Укажите правильный путь к cmd.exe на вашей системе

    # Путь к скрипту активации виртуального окружения
    activate_script = r'E:\PythonProjects\toMP3\venv\Scripts\activate'  # Укажите правильный путь к активационному скрипту

    # Открытие консоли и активация виртуального окружения
    subprocess.Popen([cmd_path, '/K', activate_script], shell=True)

    # Задержка в 5 секунд
    time.sleep(5)

    # Выполнение команды в активированной консоли
    command = ['python', 'toMp3.py'] + dropped_files
    subprocess.call(command)