import asyncio
import os
from pyrogram import Client, idle
from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
STRING = os.environ.get("STRING", "")

bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           
if STRING:
    # Create instances of the Client2 and Client classes
    client2 = Client2(STRING)
    client = Client("Renamer", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))

    # Start both instances
    client2.start()
    client.start()

    # Wait for both instances to finish processing messages
    idle()

    # Stop both instances
    client2.stop()
    client.stop()
else:
    # Start the Client instance
    client = Client("Renamer", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))
    client.run()
    bot.run()
