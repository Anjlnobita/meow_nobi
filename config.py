import re
import os
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


YTDOWNLOADER = 1
LOG_FILE_NAME = "logs.txt"
TEMP_DB_FOLDER = "nobita"
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
LOG = 2
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}


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


CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "18000")
)  # Remember to give value Seconds



DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "3000")
)  # Remember to give value in Minutes


EXTRA_PLUGINS = getenv(
    "EXTRA_PLUGINS",
    "false",
)


EXTRA_PLUGINS_REPO = getenv(
    "EXTRA_PLUGINS_REPO",
    "https://github.com/anjlnobita/neow",
)

EXTRA_PLUGINS_FOLDER = getenv("EXTRA_PLUGINS_FOLDER", "plugins")

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1000")
) 

# Token allow for access youtube songs. [ True = use token data, False = use cookies ]
TOKEN_ALLOW = os.getenv("TOKEN_ALLOW", "true")

# Auto Gcast/Broadcast Handler, Write:- [On / Off] During Hosting.
AUTO_GCAST = os.getenv("AUTO_GCAST", "on")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")


# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "1"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "1"))



# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "999"))


# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "500"))


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "1073741824")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
) 

SET_CMDS = getenv("SET_CMDS", "False")





DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )


if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )