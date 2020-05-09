#Let it decide edit or reply for sudo filters
#😂🤣
from sample_config import Config

def edit_or_reply(client, user_id, text):
    if user_id in Config.SUDO_USERS:
        return client.reply(text)
    else:
        return client.edit(text)
