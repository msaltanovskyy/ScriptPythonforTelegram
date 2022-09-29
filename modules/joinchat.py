import time
from pyrogram.errors import FloodWait, ChannelPrivate, ChannelInvalid, BadRequest
from loguru import logger
from colorama import Fore

from main import main

chat_id = list(map(str, input(Fore.GREEN + "\032 Название чатов(@chatname без @,через запятую): ").split(",")))


def join_to_chat(app):
    with app:
        for chat in chat_id:
            try:
                app.join_chat(chat)
                logger.info(f"Join to chat |{chat}|")
            except FloodWait as f:
                logger.error(f"Pause flood wait {f.value}")
                time.sleep(f.value)
            except ChannelPrivate:
                logger.error(f"Chanel is private |{chat}|")
            except ChannelInvalid:
                logger.error(f"Chanel is invalid |{chat}|")
            except BadRequest:
                logger.error(f"Entry error |{chat}|")
            except:
                pass

        else:
            print(Fore.YELLOW + "Завершено!!!")
            main()
