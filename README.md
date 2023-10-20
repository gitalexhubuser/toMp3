# toMP3

![](Images/Logo.png)

## Описание

Этот проект - это конвертер **видео** файлов в **аудио** (формат mp3)

А так же перекодировщик ***.mp4** файлов в ***.mp4** (но с другим кодеком)

> Это нужно, чтоб можно было импортировать видео в Adobe Premiere Pro без **ошибки кодека av01**

![](Images/av01.png)

---

## Использование

Чтоб воспользоватся данным продуктом:

- Читаем [README.md](https://github.com/gitalexhubuser/toMp3#%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0) (пункт с установкой)
    - Создаём и настраиваем `venv`
    - Устанавливаем список библиотек из `requirements.txt`

- Если всё уже установлено:
    - Изменяем путь в bat на ваш `E:\PythonProjects\toMP3`
    - Запускаем `toMp3.bat`
    - Перетаскиваем файл в открытую `cmd` (технология Drag'n'Drop)
    - Жмём `Enter`

Из особенностей:
- Библиотека moviepy - **не** устанавливается глобально в систему! Используется виртуальное окружение.

[Конвертер файлов по одному](https://youtu.be/b8Apnfi1H8U)

[Конвертер файлов целой папкой](https://youtu.be/mIWgtYCkux0)

[Пруф, что moviepy не установлена в систему](https://youtu.be/gPL59fBfUKs)

[Решение проблемы с кодировкой av01](https://youtu.be/h28vVPzJsBQ)

---

## Установка

- Для работы скрипта `Python` должен быть в системе!

> python-3.8.7-amd64 Win7

> python-3.12.0-amd64 Win10

- `python -m venv venv`

- `pip install -r requirements.txt`

---

## Старый скрипт

```bash
# Старый скрипт (если стоит ffmpeg в PATH)
# any mp4 to mp3 (no pause)
del *.mp3
for %%a in ("*.mp4") do ffmpeg -i "%%a" "%%~na.mp3"
```

---

# Репо
| Описание | Ссылка |
| ------ | ------ |
Репо: | [github.com/gitalexhubuser/toMp3](https://github.com/gitalexhubuser/toMp3)
