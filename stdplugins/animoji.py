''' Available Commands::
- .lmoon
- .hi
- .cheer
- .getwell
- .luck
- .sprinkle
- .love
BY : @PhycoNinja13b'''

from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd
from misc.edit_or_reply import edit_or_reply

@borg.on(admin_cmd(pattern=r"lmoon", allow_sudo=True))
async def test(event):
    if event.fwd_from:
        return 
    await edit_or_reply(event, event.from_id, "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕")

# @PhycoNinja13b 's Part begin from here

@borg.on(admin_cmd(pattern=r"hi", allow_sudo=True))
async def hi(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, event.from_id, "🌺✨✨🌺✨🌺🌺🌺\n🌺✨✨🌺✨✨🌺✨\n🌺🌺🌺🌺✨✨🌺✨\n🌺✨✨🌺✨✨🌺✨\n🌺✨✨🌺✨🌺🌺🌺\n☁☁☁☁☁☁☁☁")

@borg.on(admin_cmd(pattern=r"cheer", allow_sudo=True))
async def cheer(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, event.from_id, "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐")

@borg.on(admin_cmd(pattern=r"getwell", allow_sudo=True))
async def getwell(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, event.from_id, "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹")

@borg.on(admin_cmd(pattern=r"luck", allow_sudo=True))
async def luck(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, event.from_id, "💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚")

@borg.on(admin_cmd(pattern=r"sprinkle", allow_sudo=True))
async def sprinkle(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, event.from_id, "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀")

@borg.on(admin_cmd(pattern=r"work", allow_sudo=True))
async def work(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, event.from_id, "📔📚                  📚\n📓📚📖  😫  📚📚📓\n📕📚📚  📝  📗💻📘\n📖📖📖📖📖📖📖📖\nDoing my work!\n✏️📝✏️📝✏️📝✏️📝\n")

@borg.on(admin_cmd(pattern=r"love", allow_sudo=True))
async def love(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, event.from_id, "🥰 🥰      🥰    🥰🥰         🥰\n🥰 🥰      🥰    🥰  🥰     🥰  \n🥰 🥰      🥰    🥰   🥰  🥰    \n🥰 🥰🥰 🥰🥰🥰      🥰 _    \n\n\n            🥰     🥰        ♥    ♥   \n            🥰     🥰   ♥    ♥    ♥\n            🥰     🥰      ♥       ♥   \n            🥰🥰🥰            ♥         \n")
