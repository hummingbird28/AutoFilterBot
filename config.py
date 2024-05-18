import re
from os import environ
from dotenv import load_dotenv

load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Bot settings
USE_DESCRIPTION_FILTER = bool(environ.get("USE_DESCRIPTION_FILTER", True))
PICS = (
    environ.get(
        "PICS",
        "https://telegra.ph/file/8b42f6caf6ef5fd76766f.jpg https://telegra.ph/file/82b5bbbab6d5e5593b6b2.jpg",
    )
).split()

TMDB_KEY = environ.get("TMDB_KEY")

# Admins, Channels & Users
ADMINS = [int(admin) for admin in environ.get("ADMINS", "").split()]
CHATS = [str(ch) for ch in environ.get("CHATS", "0").split()]
COMMUNITIES = [str(ch) for ch in environ.get("COMMUNITIES", "0").split()]


DATABASE_URI = environ.get("DATABASE_URI", "")
DATABASE_NAME = environ.get("DATABASE_NAME", "switch_movie_bot")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "switch_files")

# Others
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", 0))
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "")
P_TTI_SHOW_OFF = is_enabled((environ.get("P_TTI_SHOW_OFF", "True")), True)
IMDB = is_enabled((environ.get("IMDB", "True")), True)
SINGLE_BUTTON = is_enabled((environ.get("SINGLE_BUTTON", "True")), True)
CUSTOM_FILE_CAPTION = environ.get(
    "CUSTOM_FILE_CAPTION", "<code>{file_name}</code>\n\n<b>Size:</b> {file_size}\n\n"
)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get(
    "IMDB_TEMPLATE",
    "<b>🎬 Title:</b> <a href='{url}' target='_blank'>{title}</a> [{year}] —<b>{kind}</b>\n\n<b>📆 Release:</b> <a href='{url}/releaseinfo'  target='_blank'>{release_date}</a>\n<b>🌟 Rating:</b> <a href='{url}/ratings'  target='_blank'>{rating} / 10</a>\n(based on <code>{votes}</code> user ratings.)\n\n<b>🎭 Genres:</b> #{genres}\n<b>📀 Runtime:</b> <code>{runtime} minutes</code>\n\n<b>☀️ Languages:</b> #{languages}\n<b>🌎 Country of Origin:</b> #{countries}\n<b>🎥 Director:</b> {director}\,n\n<b>",
)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get("INDEX_REQ_CHANNEL", LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get("FILE_STORE_CHANNEL", "")).split()]
MELCOW_NEW_USERS = is_enabled((environ.get("MELCOW_NEW_USERS", "True")), True)
PROTECT_CONTENT = is_enabled((environ.get("PROTECT_CONTENT", "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get("PUBLIC_FILE_STORE", "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += (
    "IMDB Results are enabled, Bot will be showing imdb details for you queries.\n"
    if IMDB
    else "IMBD Results are disabled.\n"
)
LOG_STR += (
    "P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n"
    if P_TTI_SHOW_OFF
    else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n"
)
LOG_STR += (
    "SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n"
    if SINGLE_BUTTON
    else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n"
)
LOG_STR += (
    f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n"
    if CUSTOM_FILE_CAPTION
    else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n"
)
LOG_STR += (
    "Long IMDB storyline enabled."
    if LONG_IMDB_DESCRIPTION
    else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n"
)
LOG_STR += (
    "Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n"
    if SPELL_CHECK_REPLY
    else "SPELL_CHECK_REPLY Mode disabled\n"
)
LOG_STR += (
    f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n"
    if MAX_LIST_ELM
    else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n"
)
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

JOIN_COMMUNITY_USER = environ.get("JOIN_COMMUNITY_USERNAME", default="")
INDEX_COMMUNITY_ID = environ.get("INDEX_COMMUNITY_ID", default="")
INDEX_CHANNEL_ID = environ.get("INDEX_CHANNEL_ID", default="")