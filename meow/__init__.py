import json
import os

from meow.core.bot import nobita
from meow.core.dir import dirr
from meow.core.git import git
from meow.core.userbot import userbot
from meow.core.youtube import nobii
from meow.misc import dbb, heroku
import config 





import config
from .logging import LOGGER

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