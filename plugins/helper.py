# (c) HeimanPictures
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START = """
Hi {}!
        
This Is PDisk Bot For Free 😇
Read /help Carefully & Do Follow All Given Instruction...

For More Movies Join @NklRockers
"""

HELP = """
**Send Me Direct Download Link Like Mirror Or From @DirectLinkGeneratorbot.

Send As This Format**

`link | Title`

**Or**

`Video link | Title | Thumbnail link`

**NOTE:
➢ Do Not Spam, Send Link One By One
➢ To Know Status Just Go To cofilink.com/home
➢ Join Our Channel @NklRockers**
"""

ABOUT = """
Hi!
        
This Is PDisk Bot Made By @NklRockers Team

For More Movies Join @NklRockers
"""

# NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel Linkz', url='https://telegram.dog/NklRockers'),
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel Linkz', url='https://telegram.dog/NklRockers'),
        ],[
        InlineKeyboardButton('Share Now', url='https://telegram.dog/share/url?url=https://telegram.dog/Pdisk_Uploader_Nkl_Bot'),
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel Linkz', url='https://telegram.dog/NklRockers'),
        ]]
    )



@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=START,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )


@Client.on_message(filters.command('help') & filters.private)
async def help(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
