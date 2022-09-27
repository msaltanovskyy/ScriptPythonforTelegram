from colorama import Fore
import time as t

from main import main
from setting import sort_file, Pause
from loguru import logger

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@@@@@@Скрипт для отправлений приглашений на канал@@@@@@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

sort_file()
print(Fore.YELLOW+"Сортировка id из файла...")
t.sleep(5)
print(Fore.YELLOW + "@@@@@@@@@@@@@@@README@@@@@@@@@@@@@@@@@@@@\n"
      "В файле temp находятся все спарсеные id,\n",
      "необходимо скопировать и вставить\n",
      Fore.RED+"(без квадратных кавычек)\n",
      "или вставить собственные")
user_id = list(map(int, input(Fore.GREEN + "\032 Id пользователей (через запятую): ").split(",")))
chat_id = input("Введите id канала: ")


def Inviter(app):
    with app:
        for users in user_id:
            logger.info(f"User added to group - id| {users} |")
            app.add_chat_members(chat_id, users)
            Pause()
        else:
            print(Fore.YELLOW + "Завершено!!!")
            main()
