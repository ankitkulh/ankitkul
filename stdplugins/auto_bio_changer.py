# For @UniBorg
# (c) Shrimadhav U K
"""Auto Profile Updation Commands
.autopp"""
import asyncio
import time
from telethon import functions
from telethon.errors.rpcerrorlist import FloodWaitError
from uniborg.util import admin_cmd


DEL_TIME_OUT = 70


@borg.on(admin_cmd("autobio"))  
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"time{HM} UTC "
        logger.info(bio)
        try:
            await borg(functions.account.UpdateProfileRequest(  
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await borg.send_message(  
            #     Config.PRIVATE_GROUP_BOT_API_ID,  
            #     "Changed Profile Picture"
            # )
        await asyncio.sleep(DEL_TIME_OUT)

