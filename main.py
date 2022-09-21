from colorama import Fore
from pyrogram.handlers import MessageHandler, UserStatusHandler, RawUpdateHandler

from modules import auth

app = auth.auth_user()


def main():
    select = input(Fore.GREEN +"\032 1. Реакции на сообщения\n"
                   "\032 2. Парсер пользователей по сообщениям\n"
                    "\032 3. Инвайтер\n"
                   "Введите число: ")
    if select == "1":
        from modules import reaction
        app.add_handler(MessageHandler(reaction.reaction_massage))
        app.run()
    elif select == "2":
        from modules import parseuser
        app.add_handler(MessageHandler(parseuser.parseUserMy))
        app.run()
    elif select == "3":
        from modules import inviter
        app.add_handler(inviter.Inviter)
        app.run()
    elif select == "4":
        from modules import spam
        app.add_handler(UserStatusHandler(spam.spamBot))
        app.run()
    else:
        print("Команда не найдена")
        main()



if __name__ == '__main__':
    main()

