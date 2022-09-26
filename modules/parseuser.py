from pathlib import Path

from colorama import Fore
from loguru import logger

from setting import add_group, check_file

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@@@@@@Скрипт для парсинга пользователей из каналов@@@@@@@\n "
                   "@@@@@@@@@@@по последним отправленым сообщениям@@@@@@@@@@@@@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

group = add_group()
filename = check_file(directory="parseuser", extension="json")


def parseUserMy(app, messages):
    try:
        if messages.chat.id in group:  # если ID чата есть в списке то:
            logger.info(f"FIND NEW USER | {messages.chat.id}| {messages.from_user.username} || {messages.from_user.id}")
            users = app.get_chat_member(messages.chat.id, messages.from_user.id)
            path = Path("parseuser", f"{filename}.json")
            file = open(path, "a")
            file.writelines(f"\n{users['user']},\n]\r")
            file.close()
        else:
            logger.error(f"FUCK | {messages.chat.id}")
    except:
        pass

