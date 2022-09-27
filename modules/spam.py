from colorama import Fore

from main import main
from setting import Pause
from loguru import logger

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@@@@@@@@@@@@@@@@@@@@@SPAM-BOT@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


text = input("Введите сообщение: ")
user_count = list(map(int, input(Fore.GREEN + "\032 Id пользователей (через запятую): ").split(",")))
list_len = len(user_count)
print(f"Количество пользователей: {list_len}")


def spamBot(app):
    with app:
        for users in user_count:
            logger.info(f"Messages send - id| {users} |")
            app.send_message(users, f"{text}", protect_content=True)
            Pause()
        else:
            print(Fore.YELLOW + "Завершено!!!")
            main()


