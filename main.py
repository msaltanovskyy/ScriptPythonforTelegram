import time

from colorama import Fore
from pyrogram.handlers import MessageHandler

from modules import auth


def main():
    app = auth.auth_user()
    print(Fore.LIGHTRED_EX + "Выбирите команду для старта (0-6)")
    select = input(Fore.GREEN + "\032 1. Реакции на сообщения\n"
                                "\032 2. Парсер пользователей по сообщениям\n"
                                "\032 3. Инвайтер\n"
                                "\032 4. Спам-бот\n"
                                "\032 5. Вступление в чаты\n"
                                "\032 0. Выход\n"
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
        inviter.Inviter(app)
        app.run()
    elif select == "4":
        from modules import spam
        spam.spamBot(app)
        app.run()
    elif select == "5":
        from modules import joinchat
        joinchat.join_to_chat(app)
        app.run()
    elif select == "0":
        print(Fore.LIGHTRED_EX + "Работа программы завершена....")
        time.sleep(3)
        quit()
    else:
        print("Команда не найдена")
        main()


if __name__ == '__main__':
    main()
