from swibots import BotApp, BotContext, CommandEvent
from client import app

@app.on_command("echo")
async def echo_command(ctx: BotContext[CommandEvent]):
        txt = ctx.event.params
        if txt == "" or txt is None:
            txt = "Nothing to echo! :/"
        await ctx.event.message.reply_text(txt)