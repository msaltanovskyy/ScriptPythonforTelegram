from colorama import Fore
from pyrogram import Client


def auth_user():
    api_id = int(input("Api_id: "))
    api_hash = input("Api_hash: ")
    if len(api_hash) == 0 or api_id is None:
        print(Fore.RED + "Пустое поле!!!")
        api_id = int(input("Api_id: "))
        api_hash = input("Api_hash: ")
    app = Client(f"session", workdir='./session', api_id=api_id, api_hash=api_hash)
    return app
