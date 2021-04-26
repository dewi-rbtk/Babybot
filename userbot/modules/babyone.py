from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern='^.hai(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Hai ,  Assalamualaikum**")
    sleep(1)
    await typew.edit("Kalian Nungguin aku gak??")
    sleep(1)
    await typew.edit("Ih ga mauðŸ¤¢")
    sleep(1)
    await typew.edit("gasukaaðŸ˜«")
    sleep(1)
    await typew.edit("__GELAYY__ðŸ¤®")
    
   
@register(outgoing=True, pattern='^.knln(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("Nama Aku Amelia")
    sleep(2)
    await typew.edit("Dan Aku Cantik,")
    sleep(2)
    await typew.edit("Yuk PC Aku, Langsung Cek Profil Aku Ya")              
    sleep(2)
    await typew.edit("**I LOVE YOU**")
    
@register(outgoing=True, pattern='^.citra(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("Haii !!")
    sleep(2)
    await typew.edit("Aku Nama Aku Citra,")
    sleep(2)
    await typew.edit("Yang Paling Cantik")              
    sleep(2)
    await typew.edit("Macam Bidadari")
    sleep(2)
    await typew.edit("**Mwah💋**")


@register(outgoing=True, pattern='^.alay(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("eh kamu, iya kamu")
    sleep(1)
    await typew.edit("**ALAY** bnget sih")
    sleep(1)
    await typew.edit("spam bot mulu")
    sleep(1)
    await typew.edit("baru jadi userbot ya?? xixixi")
    sleep(1)
    await typew.edit("pantes **NORAK**")


CMD_HELP.update({
    "animasi1":
    "`.hai` ; `.knln` ; `.alay` ; `.citra`\
    \nUsage: Vip Khusus Buat Kamu!"
})
