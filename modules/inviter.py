from colorama import Fore

from modules.auth import auth_user
from setting import sort_file
from loguru import logger

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@@@@@@Скрипт для отправлений приглашений на канал@@@@@@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

app = auth_user("invateSession")


def Inviter():
    chat_id = input("Введите id канала: ")
    link = app.create_chat_invite_link(chat_id)
    user_id = sort_file()
    for user in user_id:
        app.add_chat_members(user, link)
        logger.info(f"User added to group - id| {user} |")

