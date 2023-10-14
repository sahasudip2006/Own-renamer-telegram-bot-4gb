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
    await message.reply_text(f"Origional BOT: <a href='http://t.me/S_4GB_RENAME_PRO_BOT'>BOT_NAME</a>\n"
                              f"Creator: <a href='https://t.me/SUDIPSAHA06'>Original Dev</a>\n" #don't remove this
                              f"Language: Python3\n"
                              f"Library: Pyrogram 2.0\n"
                              f"Server: KOYEB\n"
                              f"Total Renamed File: {total_rename}\n"
                              f"Total Size Renamed: {humanbytes(int(total_size))}\n\n"
                              f"Thank you by owner <a href='https://t.me/OWNER_USERNAME'>OWNER_NAME</a> for your hard work\n\n"
                              f"Love from<a href='https://t.me/SUDIPSAHA06, or BOT_USERNAME'>**OWNER_NAME, or BOT_NAME**</a> ❤️", quote=True)

if __name__ == '__main__':
    bot.run()
