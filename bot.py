import datetime
from pyrogram import Client,filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        text=f"**Hi {message.chat.first_name}!** \n\nThis is **Bestz URL Shorter Bot**. Just send me any big link and get short link.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Bots Updates Channel', url='https://t.me/naijabestz')
                ],
                [
                    InlineKeyboardButton('Support Group', url='https://t.me/naija_bestz')
                ]
            ]
        )
    )
