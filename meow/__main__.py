import asyncio
import importlib
from telegram.ext import Application

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, filters

from pyrogram import idle

import config
from config import BANNED_USERS
from meow import HELPABLE, LOGGER, app, userbot
#from meow.core.call import meow
from meow.plugins import ALL_MODULES
from meow.utils.database import get_banned_users, get_gbanned
from meow.misc import sudo

application = Application.builder().token(config.BOT_TOKEN).build()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("meow").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("meow.plugins").info("Successfully Imported All Modules ")

    await userbot.start()
    #await nobi.start()
    #await nobi.decorators()
    LOGGER("meow").info("meow successfully started ")
    await idle()

def main() -> None:
    """Run bot."""


    application.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("meow").info("stopping meow meow ") 
    
    
    
    
    
    
    

      