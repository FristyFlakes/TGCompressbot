#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K


from bot.localisation import Localisation
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def new_join_f(client, message):
    # delete all other messages, except for AUTH_USERS
    #await message.delete(revoke=True)
    # reply the correct CHAT ID,
    # and LEAVE the chat
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            Localisation.WRONG_MESSAGE.format(
                CHAT_ID=message.chat.id
            )
        )
        # leave chat
        await message.chat.leave()

async def start_message(bot, message):
    await message.reply(
        text=f"**Hi, Sir!** \n\nThis is **Bestz Video Compressor**.",
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


async def help_message_f(client, message):
    # display the /help message
    await message.reply_text(
        Localisation.HELP_MESSAGE,
        quote=True
    )
