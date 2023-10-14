import os
from pyrogram import Client, filters
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes

TOKEN = os.environ.get('TOKEN', '')
BOT_ID = TOKEN.split(':')[0]

bot = Client('renamer_bot', bot_token=TOKEN)

@bot.on_message(filters.private & filters.command(['about']))
async def about_command_handler(client, message):
    botdata(int(BOT_ID))
    data = find_one(int(BOT_ID))
    total_rename = data['total_rename']
    total_size = data['total_size']
    await message.reply_text(f"Origional BOT: <a href='https://t.me/BOT_USERNAME'>BOT_NAME</a>\n"
                              f"Creator: <a href='https://t.me/SUDIPSAHA06'>🦋 Owner 🦋</a>\n" #don't remove this
                              f"Language: Python3\n"
                              f"Library: Pyrogram 2.0\n"
                              f"Server: KOYEB\n"
                              f"Total Renamed File: {total_rename}\n"
                              f"Total Size Renamed: {humanbytes(int(total_size))}\n\n", quote=True)

if name == 'main':
    bot.run()
