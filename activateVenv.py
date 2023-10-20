import subprocess

# Путь к скрипту активации виртуального окружения
activate_script = r'E:\PythonProjects\toMP3\venv\Scripts\activate'  # Укажите правильный путь к активационному скрипту

command = ['cmd.exe', '/K', activate_script, '&&', 'python', 'toMp3.py']

# Открытие консоли, активация виртуального окружения и выполнение команды
subprocess.Popen(command, shell=True)

while True:

    # Запрашиваем ввод от пользователя
    user_input = input("Введите путь к файлу (или 'выход' для выхода): ")

    # Проверка на выход
    if user_input.lower() == 'выход':
        break

    # Проверка, что пользователь ввел путь к файлу
    if not user_input:
        print("Путь к файлу не был введен.")
        continue
    
    if user_input:
        # print(user_input)
        # command = ['python', 'toMp3.py', user_input]

        # Команда для запуска нового окна командной строки с выполнением команды python script.py
        command = ['start', 'cmd', '/c', 'python', 'toMp3.py', user_input]

        subprocess.call(command) # Выполнение команды