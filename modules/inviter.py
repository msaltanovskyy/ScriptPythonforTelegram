from pyrogram.errors import BadRequest
from colorama import Fore

from main import main
from setting import Pause
from loguru import logger

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@@@@@@Скрипт для отправлений приглашений на канал@@@@@@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print(Fore.YELLOW + "@@@@@@@@@@@@@@@README@@@@@@@@@@@@@@@@@@@@\n"
      "В файле parseuser находятся все спарсеные id,\n",
      "необходимо скопировать и вставить\n",
      Fore.RED+"(без квадратных кавычек)\n",
      "или вставить собственные")


def Inviter(app):
    user_id = list(map(int, input(Fore.GREEN + "\032 Id пользователей (через запятую): ").split(",")))
    chat_id = input("Введите id канала: ")
    user = list(set(user_id))
    with app:
        for users in user:
            try:
                logger.info(f"User added to group - id| {users} |")
                app.add_chat_members(int(chat_id), users)
                Pause()
            except BadRequest:
                logger.info(f"User is not added - id |{users}|")
            except:
                pass
        else:
            print(Fore.YELLOW + "Завершено!!!")
            main()
