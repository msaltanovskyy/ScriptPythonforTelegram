import json
import os.path
import time
from pathlib import Path

from colorama import Fore
from pyrogram import Client

from setting import get_directory_script


def auth_user():
    wd = get_directory_script()
    path = Path(wd, "config.json")
    if os.path.isfile(path) is False:
        print(Fore.YELLOW + "Пройдите авторизацию!!!")
        time.sleep(2)
        api_id = input("Api_id: ")
        api_hash = input("Api_hash: ")
        json_data = (
            {
                "api_id": f"{api_id}",
                "api_hash": f"{api_hash}"
            }
        )
        with open(path, "w") as file:
            json.dump(json_data, file, indent=4)
        file.close()
        app = Client("session", workdir=f'{wd}/session', api_id=api_id, api_hash=api_hash)
        return app
    else:
        with open(path) as file:
            data = json.load(file)
            file.close()
        print(Fore.YELLOW + "АВТОРИЗАЦИЯ...")
        time.sleep(2)
        print(Fore.GREEN + "АВТОРИЗИРОВАННЫЙ...\n",
              Fore.RED + "Для авторизации нового аккаунта удалите файл config.json")
        time.sleep(2)
        app = Client(f"session", workdir=f'{wd}/session', api_id=data['api_id'], api_hash=data['api_hash'])
        return app
