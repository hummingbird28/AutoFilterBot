from dotenv import load_dotenv
import yaml
from client import app
import os
import swibots
from loader import load_modules

env_file = os.path.join(os.path.dirname(__file__), "..", ".env")  # noqa : E402
load_dotenv(env_file, override=True)

import logging.config  # noqa : E402
import logging  # noqa : E402
from swibots import BotContext, CommandEvent, CallbackQueryEvent, Message, filters
from swibots import BotCommand as RegisterCommand  # noqa : E402
from config import ADMINS

WS_URL = os.getenv("CHAT_SERVICE_WS_URL")
CONFIG_WS_URL = swibots.get_config()["CHAT_SERVICE"]["WS_URL"]

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)

app.set_bot_commands(
    [
        RegisterCommand("json", "Prints the message json", True),
        RegisterCommand("echo", "Echoes the message", True),
        #       RegisterCommand("buttons", "Shows buttons", True),0
        # media
        RegisterCommand("search", "Search for indexed media", True),
        # help
        RegisterCommand("start", "Show help about commands", True),
        # imdb
        RegisterCommand("movie", "Search for a movie on IMDb", True),
        # filters
        RegisterCommand("addfilter", "Add a filter", True),
        RegisterCommand("index", "Index current channel or group (OWNER ONLY)", True),
        RegisterCommand("deleteall", "Delete all indexed (OWNER ONLY)", True),
        RegisterCommand("listfilters", "List all filters", True),
        RegisterCommand("delfilter", "Delete a filter", True),
        RegisterCommand("delallfilters", "Delete all filters", True),
    ]
)

load_modules("plugins")


@app.on_callback_query(filters.text("close_data"))
async def on_callback_query(ctx: BotContext[CallbackQueryEvent]):
    message: Message = ctx.event.message
    await message.delete()


@app.on_command("start")
async def start(ctx: BotContext[CommandEvent]):
    message: Message = ctx.event.message
    text = (
        "Hello! here is a list of commands you can use:\n"
        + "/help - Show this message\n"
        + "/json - Dump the message as json\n"
        + "/imdb <movie name> - Search for a movie on IMDb\n"
        + "/search Search for a file on my database\n"
    )

    if message.user_id in ADMINS:
        text += (
            "\nAdmin commands:\n"
            + "/index <group or channel> - Save media files from the channel or group\n"
            + "/addfilter <filter> - Add a filter\n"
            + "/delfilter <filter> - Delete a filter\n"
            + "/listfilters - List all filters\n"
            + "/delallfilters - Delete all filters\n"
        )

    await message.reply_text(text)


app.run()
