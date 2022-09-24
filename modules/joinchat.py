from loguru import logger
from colorama import Fore
from pyrogram.types import Chat

from main import main
from setting import Pause

chat_id = list(map(int, input(Fore.GREEN + "\032 Id чатов(через запятую): ").split(",")))


def join_to_chat(app):
    with app:
        for chat in chat_id:
            Pause()
            app.join_chat(chat)
            if Chat is True:
                logger.info(f"Join to chat |{chat}|")
            else:
                logger.error(f"Failed to join chat |{chat}|")
        else:
            print(Fore.YELLOW+"Завершено!!!")
            main()
