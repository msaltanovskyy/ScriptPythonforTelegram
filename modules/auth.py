from colorama import Fore
from pyrogram import Client


def auth_user():
    app = Client("session", workdir='./session')
    return app
