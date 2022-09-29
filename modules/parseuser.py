from pathlib import Path

from colorama import Fore
from loguru import logger

from setting import add_group, check_file, get_directory_script

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@@@@@@Скрипт для парсинга пользователей из каналов@@@@@@@\n "
                   "@@@@@@@@@@@по последним отправленным сообщениям@@@@@@@@@@@@@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

group = add_group()
filename = check_file(directory="parseuser", extension="json")
wd = get_directory_script()


def parseUserMy(app, messages):
    try:
        if messages.chat.id in group:  # если ID чата есть в списке то:
            logger.info(f"FIND NEW USER | {messages.chat.id}| {messages.from_user.username} || {messages.from_user.id}")
            users = app.get_chat_member(messages.chat.id, messages.from_user.id)
            path = Path(f"{wd}", "parseuser", f"{filename}.json")
            file = open(path, "a")
            file.writelines(f"\n{users},\n]\r")
            file.close()
        else:
            logger.error(f"FUCK | {messages.chat.id}")
    except:
        pass
