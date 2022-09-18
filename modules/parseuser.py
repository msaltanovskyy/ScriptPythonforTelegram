from colorama import Fore
from loguru import logger

from modules.auth import auth_user
from setting import add_group, check_file

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@@@@@@Скрипт для парсинга пользователей из каналов@@@@@@@\n "
                   "@@@@@@@@@@@по последним отправленым сообщениям@@@@@@@@@@@@@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

app = auth_user("parseSession")
group = add_group()
check_file()


@app.on_message()
def parseUserMy(_, messages):

    try:
        if messages.chat.id in group:  # если ID чата есть в списке то:
            logger.info(f"FIND NEW USER | {messages.chat.id}| {messages.from_user.username} || {messages.from_user.id}")
            users = app.get_chat_member(messages.chat.id, messages.from_user.id)
            file = open("parseuser/parseruser.json", "a")
            file.writelines(f"\n{users},\n")
            print("\n]\r")
            file.close()
        else:
            logger.error(f"FUCK | {messages.chat.id}")
    except:
        pass


app.run()
