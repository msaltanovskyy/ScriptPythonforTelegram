from colorama import Fore
from loguru import logger

from setting import add_group, Pause

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@Скрипт для реакций на последние отправленые сообщения@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

group = add_group()


def reaction_massage(_, messages):
    try:
        if messages.chat.id in group:  # если ID чата есть в списке то:
            logger.info(f"FIND NEW MESSAGE - {messages.chat.id} | {messages.from_user.id}")
            #  if message.from_user.id in call:  можно поставить проверку на определенного человека тогда в
            #  списке call = [] нужно указать его
            Pause()
            messages.react(emoji='❤️')
        else:  # иначе:
            logger.error(f"FUCK | {messages.chat.id}")
    except:
        pass
