from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )
    

reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Support Channel', url='https://t.me/naijabestz'),
                    InlineKeyboardButton('Feedback', url='https://t.me/BestzBrothers')
                ],
                [
                    InlineKeyboardButton('Other Bots', url='https://t.me/naijabestz'),
                    InlineKeyboardButton('Source', url='https://www.9jabestz.com')
                ]
            ]
        ),
