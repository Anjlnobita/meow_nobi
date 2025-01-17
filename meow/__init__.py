import json
import os

from meow.core.bot import nobita
from meow.core.dir import dirr
from meow.core.git import git
from meow.core.userbot import userbot
from meow.core.youtube import nobii
from meow.misc import dbb, heroku

from telethon import TelegramClient
 
from .__main__ import telethn 

import config
from .logging import LOGGER

telethn = telethn()

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