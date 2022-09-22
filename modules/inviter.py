from colorama import Fore
import time as t
from setting import sort_file, Pause
from loguru import logger

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@@@@@@Скрипт для отправлений приглашений на канал@@@@@@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

sort_file()
print(Fore.YELLOW+"Сортировка id из файла...")
t.sleep(5)
print(Fore.YELLOW + "@@@@@@@@@@@@@@@README@@@@@@@@@@@@@@@@@@@@\n"
      "В файле temp находяться все спарсеные id,\n",
      "необходимо скопировать и вставить\n",
      Fore.RED+"(без квадратных кавычек)\n",
      "или всавить собственные")
user_id = list(map(int, input(Fore.GREEN + "\032 Id пользователей (через запятую): ").split(",")))
chat_id = input("Введите id канала: ")


def Inviter(app):
    with app:
        try:
            if len(chat_id) > 5:
                for users in user_id:
                    logger.info(f"User added to group - id| {users} |")
                    app.add_chat_members(chat_id, users)
                    Pause()
            else:
                print(Fore.RED + "Введите id канала")
                Inviter(app)
        except:
            pass
