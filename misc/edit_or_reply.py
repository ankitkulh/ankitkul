#Let it decide edit or reply for sudo filters
#😂🤣
from sample_config import Config
import asyncio

async def edit_or_reply(client, user_id, text):
    if user_id in Config.SUDO_USERS:
      reply_to = await client.get_reply_message()
      if reply_to:
        return await reply_to.reply(text)
      else:
        return await client.reply(text)
    else:
        return await client.edit(text)
