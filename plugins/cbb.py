#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from helper_func import get_messages

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/Crude_X'>Pʙ Aᴊᴀʏ ❤️</a>\n○ ʟᴀɴɢᴜᴀɢᴇ : <code>ᴘʏᴛʜᴏɴ 3</code>\n○ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ {__version__}</a>\n○ sᴏᴜʀᴄᴇ : <a href='https://t.me/VadaThirnu'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n○ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+09keQAMeEz02ZWU1'>ᴀᴀsʜɪʀᴠᴀᴅ ᴄɪɴᴇᴍᴀs</a> \n○ sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/mlz_botz_support'>ᴍʟᴢ ʙᴏᴛᴢ</a> ",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʜᴏᴍᴇ", callback_data = "start"),
                        InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "start":
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data = "about"),
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close")
                ]
            ]
        )
        await query.message.edit_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
    
