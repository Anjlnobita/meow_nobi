import asyncio
import importlib

from pyrogram import idle

import config
from config import BANNED_USERS
from meow import HELPABLE, LOGGER, app, userbot
from meow.core.call import meow
from meow.plugins import ALL_MODULES
from meow.utils.database import get_banned_users, get_gbanned
from meow.misc import sudo

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
    #await sudo()
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
    LOGGER("meow.plugins").info("sucessful all meow module imported ")

    await userbot.start()
    await meow.start()
    await meow.decorators()
    LOGGER("meow").info("meow started")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("meow").info("meow meow stopping")