import os
import json
import time as t

from colorama import Fore
from pathlib import Path

from main import main


# добавление id группы
def add_group():
    group = list(map(int, input(Fore.GREEN + "\032 Id групп (через запятую): ").split(",")))
    if not group:
        print("Пустое поле:")
        group = list(map(int, input(Fore.GREEN + "\032id групп (через запятую): ").split(",")))
    return group


# проверка на наличие файла
def check_file(directory, extension):
    wd = get_directory_script()
    filename = input("Введите название файла: ")
    path = Path(wd, f"{directory}", f"{filename}.{extension}")
    check = os.path.isfile(path)
    if check is False:
        f = open(path, "w+")
        f.close()
    else:
        print(Fore.RED + f"Файл с имением {filename}.json существует")
    return filename


def Pause():
    t.sleep(10)  # Пауза между проходами


# Создание папок если они отсутствуют
def create_directory():
    print(Fore.YELLOW + "Проверка наличия директорий....")
    t.sleep(2)
    # Получение полного пути к скрипту минус исполняющий файл
    wd = get_directory_script()
    path = [Path(f"{wd}", "temp"), Path(f"{wd}", "parseuser"), Path(f"{wd}", "session")]
    for folder in path:
        if os.path.exists(folder) is False:
            os.mkdir(f"{folder}")
            print(Fore.YELLOW + f"Директория {folder} не найдена и создана....")
            t.sleep(2)
        else:
            print(Fore.YELLOW + f"Директория {folder} обнаружена....")
            t.sleep(1)


# получение пути к скрипту
def get_directory_script():
    wd = os.path.abspath(__file__).replace('setting.py', '')
    return wd


# Не используется список групп
def list_group(app):
    for dialog in app.get_dialogs():
        if dialog.chat.type == "group":
            print(dialog.chat.title)
