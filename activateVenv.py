import subprocess
import sys
import os

if __name__ == "__main__":

    # Запоминание файлов, перетащенных на скрипт
    # Получение списка перетащенных файлов
    dropped_files = sys.argv[1:]
    print(dropped_files)

    # Проверка, что были перетащены файлы
    if len(dropped_files) == 0:
        print("Файлы не были перетащены на скрипт.")
        # sys.exit(1)


    # Путь к исполняемому файлу командной строки (cmd.exe)
    cmd_path = r'C:\WINDOWS\system32\cmd.exe'  # Укажите правильный путь к cmd.exe на вашей системе

    # Путь к скрипту активации виртуального окружения
    activate_script = r'E:\PythonProjects\toMP3\venv\Scripts\activate'  # Укажите правильный путь к активационному скрипту

    # Открытие консоли и активация виртуального окружения
    subprocess.call([cmd_path, '/K', activate_script])



    # Команда для выполнения в консоли
    # command = f'python toMp3.py {" ".join(dropped_files)}'

    # Запуск команды в открытой консоли
    # os.system(command)

    # Команда для выполнения в консоли
    command = ['python', 'toMp3.py'] + dropped_files

    # Запуск команды в активированном виртуальном окружении
    subprocess.call(command)