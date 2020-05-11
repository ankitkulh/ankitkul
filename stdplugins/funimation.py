""" AVAILABLE COMMANDS IN FUNIMATION:
- .degi
- .nehi
- .earth
- .heart
- .muth
- .ufo
- .hack
- .hypno
- .eye
- .call
Modified by:- @PhycoNinja13b
"""

import random, re
from uniborg.util import admin_cmd
from misc.edit_or_reply import edit_or_reply
import asyncio
from telethon import events
from collections import deque

# degi/nehi Original Code by @kirito6969 , ©[Eyepatch](https://t.me/NeoMatrix90)

@borg.on(admin_cmd(pattern="degi ?(.*)", allow_sudo=True))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        
        degi_lst = ["Wo","Degi","Tum","Ekbar","Mang","Kar","Toh","Dekho","`Wo Degi Tum Ekbar Mang Kar toh Dekho`"]
        ed = await reply_to.reply(event, event.from_id, "...")
        await asyncio.sleep(0.5)
        for i in degi_lst:
            await ed.edit(i)
            await asycio.sleep(1)

@borg.on(admin_cmd(pattern="nehi ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, event.from_id, "`Wo PaKkA DeGi Tu ManG KaR ToH DekH`")

# (c) @UniBorg
# Earth Original written by @UniBorg edit by @I_m_Rock

@borg.on(admin_cmd(pattern="earth", allow_sudo= True))
async def _(event):
    if event.fwd_from:
      return
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    ed = await edit_or_reply(event, event.from_id, "...")
    await asyncio.sleep(0.5)
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ed.edit("".join(deq))
        deq.rotate(1)

@borg.on(admin_cmd(pattern="heart ?(.*)", allow_sudo=True))

async def _(event):

    if event.fwd_from:

        return

    reply_to = await event.get_reply_message()

    animation_interval = 2

    animation_ttl = range(0, 100)

    animation_chars = [

            "🖤",

            "❤️",

            "🖤",

            "❤️",
            
            "💙",

            "💚",

            "💛",

            "🧡",

            "💜"

        ]

    ed = await edit_or_reply(event, event.from_id, "...")
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ed.edit(animation_chars[i % 9])


@borg.on(admin_cmd(pattern="muth ?(.*)", allow_sudo=True))

async def _(event):

    if event.fwd_from:

        return

    reply_to = await event.get_reply_message()

    animation_interval = 0.3

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    animation_chars = [

            "8✊️===D",

            "8=✊️==D",

            "8==✊️=D",

            "8===✊️D",

            "8==✊️=D",

            "8=✊️==D",

            "8✊️===D",

            "8===✊️D💦",

            "8==✊️=D💦💦",

            "8=✊️==D💦💦💦"

        ]

    ed = await edit_or_reply(event, event.from_id, "...")
    await asyncio.sleep(0.5)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ed.edit(animation_chars[i % 8])

@borg.on(admin_cmd(pattern="hack ?(.*)", allow_sudo=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    reply_to = await event.get_reply_message()

    animation_chars = [
        
            "`Connecting To Hacked Private Server...`",
            "`Target Selected.`",
            "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
            "`Hacking... 100%\n█████████HACKED███████████ `",
            "`Targeted Account Hacked...\n\nPay 999$ and a Plate of Biriyani To this Nigga @PhycoNinja13b To Remove This Hack`"
        ]

    ed = await edit_or_reply(event, event.from_id, "...")
    await asyncio.sleep(0.5)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ed.edit(animation_chars[i % 11])


 
@borg.on(admin_cmd(pattern="ufo ?(.*)", allow_sudo=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 22)
    reply_to = await event.get_reply_message()
    animation_chars = [
        
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n🚀⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🚀⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🚀⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚀⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",    
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚀⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛🚀\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🛸⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛",
            "⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛🚶‍♂️\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n👽⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛👽⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛👽🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "__Signal Lost....__"

 ]
    ed = await edit_or_reply(event, event.from_id, "...")
    await asyncio.sleep()
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ed.edit(animation_chars[i % 22])

@borg.on(admin_cmd(pattern="hypno ?(.*)", allow_sudo=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 15)

    reply_to = await event.get_reply_message()

    animation_chars = [
        
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
            "⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛",
            "⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜",    
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛",
            "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",
            "[👉🔴👈](t.me/phyconinja13_bot)"

 ]

    ed = await edit_or_reply(event, event.from_id, "...")
    await aayncio.sleep(0.5)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ed.edit(animation_chars[i % 15])

@borg.on(admin_cmd(pattern="eye ?(.*)", allow_sudo=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 10)

    reply_to = await event.get_reply_message()

    animation_chars = [

            "👁👁\n  👄  =====> Abey Ja Na Gandu",
            "👁👁\n  👅  =====> Abey Ja Na Madarchod",    
            "👁👁\n  💋  =====> Abey Ja Na Randi",
            "👁👁\n  👄  =====> Abey Ja Na Betichod",
            "👁👁\n  👅  =====> Abey Ja Na Behenchod",    
            "👁👁\n  💋  =====> Abey Ja Na Na Mard",
            "👁👁\n  👄  =====> Abey Ja Na Randi",
            "👁👁\n  👅  =====> Abey Ja Na Bhosdk",    
            "👁👁\n  💋  =====> Abey Ja Na Chutiye",
            "👁👁\n  👄  =====> Hi All, How Are You Guys..."
        ]
    ed = await edit_or_reply(event, event.from_id, "...")
    await asyncio.sleep(0.5)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ed.edit(animation_chars[i % 10])

@borg.on(admin_cmd(pattern="call ?(.*)", allow_sudo=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    reply_to = await event.get_reply_message()

    animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` @PhycoNinja13b ,`Please Connect me to Pavel Durov Shukla`",
            "`User Authorised.`",
            "`Calling Pavel Durov Shukla (`@durov`) At +916969696969`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`Durov: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @PhycoNinja13b",
            "`Durov: OMG!!! I Am FAN Of You Sar...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`Durov: Please Don't Thank Sar, Telegram Is Your's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`Durov: Yes Sar, There Is A Bug In Telegram v5.14.0.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`Durov: Sure Sar \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
    ]
    ed = await edit_or_reply(event, event.from_id, "...")
    await asyncio.sleep(0.5)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ed.edit(animation_chars[i % 18])
