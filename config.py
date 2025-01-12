import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")



BOT_TOKEN = getenv("BOT_TOKEN")



MONGO_DB_URI = getenv("MONGO_DB_URI")



DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1000))


LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))


OWNER_ID = int(getenv("OWNER_ID"))



HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")


HEROKU_API_KEY = getenv("HEROKU_API_KEY")


UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/anjlnobita/meow_nobi",
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)



SUPPORT_CHANNEL = getenv("https://t.me/nobi_bots")

SUPPORT_CHAT = getenv("https://t.me/anime_societyy")


AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))



SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "125"))



TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))


TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/CwU.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/CLg.jpeg"
)
PLAYLIST_IMG_URL = "https://envs.sh/CwU.jpg"
STATS_IMG_URL = "https://envs.sh/CLg.jpeg"
TELEGRAM_AUDIO_URL = "https://envs.sh/CLg.jpeg"
TELEGRAM_VIDEO_URL = "https://envs.sh/CLg.jpeg"
STREAM_IMG_URL = "https://envs.sh/CLg.jpeg"
SOUNCLOUD_IMG_URL = "https://envs.sh/CLg.jpeg"
YOUTUBE_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/CLg.jpeg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 800**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))