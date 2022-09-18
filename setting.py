import os
import json
from colorama import Fore


# добавление id группы
def add_group():
    group = list(map(int, input(Fore.GREEN + "\032id групп (через пробел): ").split()))
    if not group:
        print("Пустое поле:")
        group = list(map(int, input(Fore.GREEN + "\032id групп (через пробел): ").split()))
    return group


# проверка на наличие файла
def check_file():
    filename = input("Введите название файла: ")
    check = os.path.isfile(f"parseuser/{filename}.json")
    if check is False:
        f = open(f"parseuser/{filename}.json", "w+")
        f.write("[")
        f.close()
    else:
        print(Fore.RED + f"Файл с именним {filename}.json существует")
        check_file()


# сортировка и поиск id пользователей в parseuser/{file}.json
def sort_file():
    filename = input("Введите название файла(parseuser/filename): ")
    with open(f"parseuser/{filename}.json") as file:
        user = json.load(file)
    sort_id = []
    for userid in user:
        id = [userid['user']['id']]
        if id not in sort_id:
            #добавить отсортированые id в файл
            sort_id.append(id)
    with open(f"temp/{filename}_temp.txt", "w+") as file2: #файл с отсортиованным id
        file2.writelines(str(sort_id))
        file2.close()
        file.close()
        return sort_id




