from colorama import Fore
from loguru import logger

from modules.auth import auth_user
from setting import add_group

print(Fore.GREEN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                   "\n@@@@Скрипт для реакций на последние отправленые сообщения@@@@\n"
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

app = auth_user("reactionSession")
group = add_group()


@app.on_message()
def reaction_massage(_, messages):
    try:
        if messages.chat.id in group:  # если ID чата есть в списке то:
            logger.info(f"FIND NEW MESSAGE - {messages.chat.id} | {messages.from_user.id}")
            #  if message.from_user.id in call:  можно поставить проверку на определенного человека тогда в
            #  списке call = [] нужно указать его
            messages.react(emoji='❤️')
        else:  # иначе:
            logger.error(f"FUCK | {messages.chat.id}")
    except:
        pass


app.run()
