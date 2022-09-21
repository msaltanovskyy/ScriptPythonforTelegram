from colorama import Fore

from setting import sort_file, Pause
from loguru import logger

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@@@@@@@@@@@@@@@@@@@@@SPAMBOT@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


user_id = sort_file()
text = input("Введите сообщение: ")


def spamBot(app, user):
    try:
        logger.info(f"Messages send - id| {user_id} | status {user.status} |")
        app.send_message(user_id, f"{text}", protect_content=True)
        Pause()
    except:
        pass
