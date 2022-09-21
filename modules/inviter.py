from colorama import Fore

from setting import sort_file, Pause
from loguru import logger

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@@@@@@Скрипт для отправлений приглашений на канал@@@@@@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


def Inviter(app):
    try:
        chat_id = input("Введите id канала: ")
        if chat_id is True:
            user_id = sort_file()
            for user in user_id:
                Pause()
                app.add_chat_members(chat_id, user)
                logger.info(f"User added to group - id| {user} |")
        else:
            Inviter(app)
    except:
        pass
