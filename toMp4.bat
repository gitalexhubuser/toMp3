@REM cmd /k "cd /d E:\PythonProjects\toMP3\venv\Scripts & activate & cd /d E:\PythonProjects\toMP3 & python toMp4Main.py"
@REM cmd /k "cd /d O:\PythonProjects\toMP3\venv\Scripts & activate & cd /d O:\PythonProjects\toMP3 & python toMp4Main.py"
@REM pause




@echo off
@REM setlocal enabledelayedexpansion
:: Получить текущий диск, на котором находится скрипт
:: for %%i in ("%~dp0") do set currentDrive=%%~di
:: Запустить скрипт на текущем диске
:: cmd /k "cd /d !currentDrive!\PythonProjects\toMP3\venv\Scripts & activate & cd /d !currentDrive!\PythonProjects\toMP3 & python toMp4Main.py"
@REM pause



@echo off
setlocal enabledelayedexpansion
:: Получить текущий диск, на котором находится скрипт
for %%i in ("%~dp0") do set currentDrive=%%~di

:: Собрать путь к venv и toMp4Main.py
set "venvPath=!currentDrive!\!~dp0venv\Scripts"
set "mainScriptPath=!currentDrive!\!~dp0toMp4Main.py"

:: Запустить скрипт на текущем диске
cmd /k "cd /d !venvPath! & activate & cd /d !mainScriptPath!"
@REM pause
