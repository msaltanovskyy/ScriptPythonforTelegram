from loguru import logger
from colorama import Fore

from main import main
from setting import Pause

chat_id = list(map(int, input(Fore.GREEN + "\032 Id чатов(через запятую): ").split(",")))


def join_to_chat(app):
    with app:
        for chat in chat_id:
            Pause()
            app.join_chat(chat)
            logger.info(f"Join to chat |{chat}|")
        else:
            print(Fore.YELLOW+"Завершено!!!")
            main()
