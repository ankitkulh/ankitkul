"""
Time In Random Profile Pics.....
Command: `.autopp`

 Custom / Modified Plugin for some magical effects by this Legendary Guy @PhycoNinja13b

If U Noob Don't Play with Codes!! Learn Programming Then Come Here!! 
If u use this plugin without Permit, Then ur mama Gey! Ur father Lesbo!! 

TROJAN ALERT!!!

#curse: who ever edits this credit section will goto hell

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
from misc.edit_or_reply import edit_or_reply
import asyncio
import shutil 


FONT_FILE_TO_USE = "Fonts/DS-DIGII.ttf"
CAPTION_FONT = "Fonts/Tangerine_Bold.ttf"

@borg.on(admin_cmd(pattern="autopp ?(.*)", allow_sudo=True))
async def autopic(event):
    hmm = await edit_or_reply(event, event.from_id, "__Enabling Random Auto PfP__")
    await asyncio.sleep(1)
    await hmm.edit("**Auto Profile Pic** have been **Activated**\n **No of PPs being used:** 100")

    pln = 0 # Enough of random shit 😂🤣 Running it in sequence would be better 🤔
    while True:
        
        TELEGRAPH_MEDIA_LINKS = []
        source = open("misc/pic.txt","r")

        m = source.readlines()
        for i in range(0,len(m)-1):
          x=m[i]
          z=len(x)
          a=x[:z-1]
          TELEGRAPH_MEDIA_LINKS.append(a)

        TELEGRAPH_MEDIA_LINKS.append(m[i+1])

        END = len(TELEGRAPH_MEDIA_LINKS)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[pln]
        ERROR = "https://telegra.ph/file/b9761d390dfd1f15299c1.jpg"

        # Fix for Error:404 while downloading some pics 
        try:
            downloaded_file_name = "./ravana/original_pic.png"
            downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
            downloader.start(blocking=False)
            photo = "photo_pfp.png"
            while not downloader.isFinished():
                place_holder = None 
        # A PfP with Error:404 will be used if error arises Σ(⊙▽⊙")
        except:
            downloaded_file_name = "./ravana/original_pic.png"
            downloader = SmartDL(ERROR, downloaded_file_name, progress_bar=True)
            downloader.start(blocking=False)
            photo = "photo_pfp.png"
            while not downloader.isFinished():
                place_holder = None

        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("  Time: %H:%M:%S \nDate: %d/%m/%y ")
        caption = "//\n@\nL\na\nz\ny\nk\ni\nl\nl\nl\ne\nr\n//"
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 40)
        cafnt = ImageFont.truetype(CAPTION_FONT, 60)
        drawn_text.text((300, 20), current_time, font=fnt, fill=(230,230,255))
        drawn_text.text((10, 10), caption, font=cafnt, fill=(221,230,255))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            await asyncio.sleep(69)
        except:
            return

        pln += 1
        if pln == END:
            pln = 0
