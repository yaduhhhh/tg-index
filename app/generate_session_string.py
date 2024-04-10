import os

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = int(os.getenv('API_ID') or input("Enter your API_ID: 16419062"))
api_hash = os.getenv('API_HASH') or input("Enter your API_HASH: 874263f2a92fbc7c67b1864b0e79cc2c")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\n" + client.session.save())
