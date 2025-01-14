from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT, START_PIC
from datetime import datetime
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from helper_func import get_readable_time

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):
    if USER_REPLY_TEXT:
        # Inline keyboard buttons
        buttons = [
            [
                InlineKeyboardButton("main channel", url="https://t.me/+jFs1FWbFSvg0ZDc1"),
                InlineKeyboardButton("join", url="https://t.me/+jFs1FWbFSvg0ZDc1"),
            ],
        ]
        # Check if START_PIC is set
        if START_PIC:
            await message.reply_photo(
                photo=START_PIC,
                caption=USER_REPLY_TEXT,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        else:
            await message.reply(
                text=USER_REPLY_TEXT,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
                
