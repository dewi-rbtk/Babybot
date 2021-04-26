""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai Baby {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/melameliaaw)"
        "\n[Repo](https://github.com/dewi-rbtk/Babybot)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/dewi-rbtk/Babybot/Love/varshelper.txt)")


CMD_HELP.update({
    "babyhelper":
    "`.lhelp`\
\nPenjelasan: Bantuan Untuk Baby-Userbot.\
\n`.vars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
