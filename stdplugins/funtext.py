""" 
By :- @PhycoNinja13b
.weebify <text> 
.f <emoji|character>"""

from telethon import events
from misc.edit_or_reply import edit_or_reply
from uniborg.util import admin_cmd

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
weebyfont = ['卂', '乃', '匚', '刀', '乇', '下', '厶', '卄', '工', '丁', '长', '乚', '从', '𠘨', '口', '尸', '㔿', '尺', '丂', '丅', '凵',
             'リ', '山', '乂', '丫', '乙']

# Weebify ported from Saitama Bot

@borg.on(admin_cmd(pattern="weebify ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    pre_msg = await event.get_reply_message()
    if not args:
        args = pre_msg.text
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    if pre_msg:
        await event.delete()
        await pre_msg.reply(string)
    else:
        await edit_or_reply(event, event.from_id, string)


@borg.on(admin_cmd(pattern="payf ?(.*)", allow_sudo=True))
async def payf_(event):

    paytext = event.pattern_match.group(1)
    if not paytext:
        await edit_or_reply(event, event.from_id, "Give something u Nigga...")

    reply_to = await event.get_reply_message()
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8, paytext * 8, paytext * 2, paytext * 2, paytext * 2,
        paytext * 6, paytext * 6, paytext * 2, paytext * 2, paytext * 2,
        paytext * 2, paytext * 2)

    if reply_to:
        await event.delete()
        await reply_to.reply(pay)
    else:
        await edit_or_reply(event, event.from_id, pay) 
