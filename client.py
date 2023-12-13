from swibots import Client
import config

app = Client(
    config.BOT_TOKEN,
    plugins=dict(
        root="plugins"
    )
)

