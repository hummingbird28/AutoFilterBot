from swibots import Client
import config

app = Client(config.BOT_TOKEN, plugins=dict(root="plugins"))

async def hasJoined(user):
    if not config.JOIN_COMMUNITY_USER:
        return True
    try:
        communityId = await app.get_community(username=config.JOIN_COMMUNITY_USER)
    except Exception as er:
        print(er)
        return True
    try:
        data = await app.get_community_member(communityId.id, user)
        assert data != None
    except Exception:
        return False
    return True

