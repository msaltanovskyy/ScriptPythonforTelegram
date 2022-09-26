import os
import json
import time as t

from colorama import Fore
from pathlib import Path, PurePath


# добавление id группы
def add_group():
    group = list(map(int, input(Fore.GREEN + "\032id групп (через запятую): ").split(",")))
    if not group:
        print("Пустое поле:")
        group = list(map(int, input(Fore.GREEN + "\032id групп (через запятую): ").split(",")))
    return group


# проверка на наличие файла
def check_file(directory, extension):
    filename = input("Введите название файла: ")
    path = Path(f"{directory}", f"{filename}.{extension}")
    check = os.path.isfile(path)
    if check is False:
        f = open(path, "w+")
        f.write("[")
        f.close()
    else:
        print(Fore.RED + f"Файл с именним {filename}.json существует")
    return filename


# сортировка и поиск id пользователей в parseuser/{file}.json
def sort_file():
    filename = input("Введите название файла(parseuser/filename): ")
    path = Path("parseuser",f"{filename}.json")
    with open(path) as file:
        user = json.load(file)
    sort_id = []
    for userid in user:
        ids = [userid['user']['id']]
        if ids not in sort_id:
            # добавить отсортированые id в файл
            sort_id.append(ids)
    path2 = Path("temp", f'{filename}_temp.txt')
    with open(path2, "w+") as file2:  # файл с отсортиованным id
        file2.writelines(str(f"{sort_id,}"))
        file2.close()
        file.close()


def Pause():
    t.sleep(10)  # Пауза между проходами


def create_directory():
    print(Fore.YELLOW+"Проверка наличия диркторий....")
    t.sleep(2)
    path = [Path("temp"), Path("parseuser"), Path("session")]
    for dir in path:
        if os.path.exists(dir) is False:
            os.mkdir(f"{dir}")
            print(Fore.YELLOW + f"Директория {dir} не найдена и создана....")
            t.sleep(2)
        else:
            print(Fore.YELLOW + f"Директория {dir} обнаружена....")
            t.sleep(2)

# Не используеться
def list_group(app):
    for dialog in app.get_dialogs():
        if dialog.chat.type == "group":
            print(dialog.chat.title)
