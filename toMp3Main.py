import subprocess

while True:

    # Запрашиваем ввод от пользователя
    user_input = input("Введите путь к файлу: ")

    # Проверка, что пользователь ввел путь к файлу
    if not user_input:
        print("Путь к файлу не был введен.")
        continue
    
    if user_input:
        # Передача данных из input в качестве аргумента команды
        command = ['python', 'toMp3.py', '--input', user_input]
        subprocess.call(command, shell=True)
