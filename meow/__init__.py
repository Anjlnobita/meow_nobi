import json
import os

from meow.core.bot import nobita
from meow.core.dir import dirr
from meow.core.git import git
from meow.core.userbot import userbot
from meow.core.youtube import nobii
from meow.misc import dbb, heroku

import config
from .logging import LOGGER

api_id = config.API_ID
api_hash = config.API_HASH
bot_token = config.BOT_TOKEN


telethn = TelegramClient("hinata", api_id, api_hash)





dirr()
git()
dbb()
heroku()
nobii()
app = nobita()
userbot = userbot()




from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}