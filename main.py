from colorama import Fore


def main():

    select = input(Fore.GREEN +"\032 1. Реакции на сообщения\n"
                   "\032 2. Парсер пользователей по сообщениям\n"
                    "\032 3. Инвайтер\n"
                   "Введите число: ")
    if select == "1":
        from modules import reaction
        reaction.reaction_massage()
    elif select == "2":
        from modules import parseuser
        parseuser.parseUserMy()
    elif select == "3":
        from modules import inviter
        inviter.Inviter()
        print("Inviter")
    else:
        print("Команда не найдена")



if __name__ == '__main__':
    main()

