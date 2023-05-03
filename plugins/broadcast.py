import os
import time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import get_id, delete_id


ADMIN = int(os.environ.get("ADMIN", 1484670284))


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("broadcast"))
async def broadcast(client, message):
    reply_message = message.reply_to_message
    if not reply_message:
        await message.reply_text("Please reply to a message to broadcast.")
        return

    message_text = "Getting all IDs from database... Please wait"
    msg = await message.reply_text(message_text)

    ids = get_id()
    total = len(ids)
    success = {}
    failed = {}

    message_text = f"Starting broadcast... Sending message to {total} users"
    await msg.edit(message_text)

    for chat_id in ids:
        try:
            await reply_message.copy(chat_id)
            success += 1
        except:
            failed += 1
            delete_id(chat_id)
        finally:
            message_text = f"Message sent to {success} chats. {failed} chats failed to receive message. Total - {total}"
            try:
                await msg.edit(message_text)
            except FloodWait as e:
                await asyncio.sleep(e.x)
