"""COMMAND : .runs , .metoo , .pro, .chase, .abuse, .belo, .tips """

from telethon import events
import random, re
from uniborg.util import admin_cmd
from misc.edit_or_reply import edit_or_reply

METOOSTR = [
    "`Me too thanks`",
    "`Haha yes, me too`",
    "`Same lol`",
    "`Me `",
    "`Same here`",
    "`Haha yes`",
    "`Same pinch `",
]
RUNSREACTS = [
    "`Runs to Thanos`",
    "`Runs to Modiji For Achey Din`",
    "`Runs far, far away from earth`",
    "`Running faster than usian bolt coz I'mma Bot`",
    "`Runs to no one`",
    "`This Group is too cancerous to deal with.`",
    "`Cya boss`",
    "`I am a mad person. Plox Ban me.`",
    "`I go away`",
    "`I am just walking off, coz me is too healthy.`",
    "`I switch off!`",
    "`I am just walking off, coz me is too fat.`",
    "`I Fugged off!`",
    "`Will run for chocolate.`",
    "`I run because I really like food.`",
    "`Running...\nbecause dieting is not an option.`",
    "`Wicked fast runnah`",
    "`If you wanna catch me, you got to be fast...\nIf you wanna stay with me, you got to be good...\nBut if you wanna pass me...\nYou've got to be kidding.`",
    "`Anyone can run a hundred meters, it's the next forty-two thousand and two hundred that count.`",
    "`Why are all these people following me?`",
    "`Are the kids still chasing me?`",
    "`Running a marathon...there's an app for that.`"
]
CHASE_STR = [
    "`Where do you think you're going?`",
    "`Huh? what? did they get away?`",
    "`ZZzzZZzz... Huh? what? oh, just them again, nevermind.`",
    "`Get back here!`",
    "`Not so fast...`",
    "`Look out for the wall!`",
    "`Don't leave me alone with them!!`",
    "`You run, you die.`",
    "`Jokes on you, I'm everywhere`",
    "`You're gonna regret that...`",
    "`You could also try /punchme, I hear that's fun.`",
    "`Go bother someone else, no-one here cares.`",
    "`You can run, but you can't hide.`",
    "`Is that all you've got?`",
    "`I'm behind you...`",
    "`You've got company!`",
    "`We can do this the easy way, or the hard way.`",
    "`You just don't get it, do you?`",
    "`Yeah, you better run!`",
    "`Please, remind me how much I care?`",
    "`I'd run faster if I were you.`",
    "`That's definitely the droid we're looking for....",
    "`May the odds be ever in your favour.`",
    "`Famous last words.`",
    "And they disappeared forever, never to be seen again.",
    "\"Oh, look at me! I'm so cool, I can run from a userbot!\" - this person",
    "Yeah yeah, just tap /punchme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
    "Legend has it, they're still running.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "It's funny, because no one cares.",
    "Ah, what a waste. I liked that one.",
    "Frankly, my dear, I don't give a damn.",
    "My milkshake brings all the boys to yard... So run faster!",
    "You can't HANDLE the truth!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "Han shot first. So will I.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
]
PRO_STRINGS = [
     "`You is pro user.`",
     "`Pros here -_- Time to Leave`",
     "`Pros everywhere`",
     "`This gey pru as phak`"
]
INSULT_STRINGS = [ 
    "`Owww ... Such a stupid idiot.`",
    "`BC.. Gaand na fulao, maa chod denge tumhari`",
    "`Don't drink and type.`",
    "`Command not found. Just like your brain.`",
    "`Bot rule 544 section 9 prevents me from replying to stupid humans like you.`",
    "`Sorry, we do not sell brains.`",
    "`Believe me you are not normal.`",
    "`I bet your brain feels as good as new, seeing that you never use it.`",
    "`If I wanted to kill myself I'd climb your ego and jump to your IQ.`",
    "`You didn't evolve from apes, they evolved from you.`",
    "`What language are you speaking? Cause it sounds like bullshit.`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn. You just live.`",
    "`Keep talking, someday you'll say something intelligent!.......(I doubt it though)`",
    "`Everyone has the right to be stupid but you are abusing the privilege.`",
    "`I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.`",
    "`You should try tasting cyanide.`",
    "`You should try sleeping forever.`",
    "`Pick up a gun and shoot yourself.`",
    "`Try bathing with Hydrochloric Acid instead of water.`",
    "`Go Green! Stop inhaling Oxygen.`",
    "`God was searching for you. You should leave to meet him.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`People like you are the reason we have middle fingers.`",
    "`When your mom dropped you off at the school, she got a ticket for littering.`",
    "`You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.`",
    "`If you’re talking behind my back then you’re in a perfect position to kiss my a**!.`",
]
ABUSE_STRINGS = [
    "Fuck off",
    "Stfu go fuck yourself",
    "Ur mum gey",
    "Ur dad lesbo",
    "Bsdk",
    "Nigga",
    "Ur granny tranny",
    "you noob",
    "Relax your Rear,ders nothing to fear,The Rape train is finally here",
    "Stfu bc",
    "Stfu and Gtfo U nub",
    "GTFO bsdk",
    "CUnt",
    " Gay is here",
    "Ur dad gey bc ",
    "Don't teach daddy how to make babies",
    "I don't have authority to chat with an asshole, Apologies",
    "You are a disappointment for ur parents, oh... Wait u were adopted. XD",
    "Not in a mood to abuse, I ain't gonna use my database on that shit guy.",
    "Ya Nigga, Ur daddy is here gibe me ur mommy",
    "🐶💿🔑 (This requires brain, which unfortunately u don't have. :')",
    "`Error:404 This nigga is gey af, my system can't handle such gayness.` \n**Bot Quiting**",
    "╭∩╮",
    "╭∩╮(-_-)╭∩╮",
    "┌∩┐(◣_◢)┌∩┐",
    "╭∩╮（︶︿︶）╭∩╮",
    "`Madharchod`",
    "`Gaandu`",
    "`Chutiya he rah jaye ga`",
    "`Ja be Gaandu`",
    "`Teri Ma ka Bhodsa madharchod`",
    "`You MotherFukcer`",
    "`You Betichod`",
    "`you are lodu no.1",
    "`Muh Me Lega Bhosdike ?`"
]
# ==========================================


@borg.on(admin_cmd(pattern="belo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    ed = await edit_or_reply(event, event.from_id, "Lemme Get Something Logical" )
    # Subscribe To @BeingLogical 🌚🤧 
    l = await event.client.get_messages(entity="@BeingLogical")
    logic = random.choice(l)
    await ed.edit(str(logic.message))
               
@borg.on(admin_cmd(pattern="abuse", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, event.from_id, random.choice(ABUSE_STRINGS))

@borg.on(admin_cmd(pattern="chase", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, event.from_id, random.choice(CHASE_STR))

@borg.on(admin_cmd(pattern="runs",allow_sudo=True))
async def _(event):
    if event.fwd_from:
         return
    reply_text = random.choice(RUNSREACTS)
    await edit_or_reply(event, event.from_id, reply_text)

@borg.on(admin_cmd(pattern="metoo",allow_sudo=True))
async def _(event):
    if event.fwd_from:
         return
    
    reply_text = random.choice(METOOSTR)
    await edit_or_reply(event, event.from_id, reply_text)	  
			  
@borg.on(admin_cmd(pattern="pro",allow_sudo=True))
async def _(event):
    if event.fwd_from:
         return
    reply_text = random.choice(PRO_STRINGS)
    
    await edit_or_reply(event, event.from_id, reply_text)

@borg.on(admin_cmd(pattern="insult",allow_sudo=True))
async def _(event):
    if event.fwd_from:
         return
    reply_text = random.choice(INSULT_STRINGS)
    
    await edit_or_reply(event, event.from_id, reply_text)
			  

@borg.on(admin_cmd(pattern="tips", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    ed = await edit_or_reply(event, event.from_id, "Lemme Fetch ya some Pro Tip" )
    # Subscribe To @Interesting_Knowledge 🌚🤧 
    l = await event.client.get_messages(entity="@Interesting_Knowledge")
    tips = random.choice(l)
    tip = str(tips.message)
    while "Pro Tip" not in tip:
      tips = random.choice(l)
      tip = str(tips.message)
    await ed.edit(tip)
