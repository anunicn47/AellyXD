from time import sleep
from AellyXD import CMD_HANDLER as cmd
from AellyXD import CMD_HELP
from AellyXD.ayiin import ayiin_cmd, edit_or_reply


@ayiin_cmd(pattern="teemo(?: |$)(.*)")
async def _(teemo):
    yins = await edit_or_reply(teemo, "`๐๐๐๐ข๐ข๐ค๐ค ๐๐ช๐ก๐ช ๐๐ช ๐`")
    sleep(2)
    await yins.edit("`๐๐๐๐๐๐ฃ ๐๐ช๐๐ ๐๐๐๐๐  ๐`")
    sleep(1)
    await yins.edit("`๐๐๐ฅ๐ ๐๐๐ก๐ค ๐๐ช ๐๐๐๐๐๐ฃ, ๐๐๐ช๐ฃ๐-๐๐๐ช๐ฃ๐๐ฃ๐ฎ๐ ๐๐ช๐๐ ๐๐๐ฃ๐ ๐๐๐ค๐จ๐ฉ๐๐ฃ๐ ๐คฃ`")


@ayiin_cmd(pattern="give(?: |$)(.*)")
async def _(giveaway):
    ayiin = await edit_or_reply(giveaway, "`๐๐ฎ๐๐ง๐๐ฉ ๐๐ ๐ช๐ฉ ๐๐๐ฅ๐๐๐ฌ๐๐ฎ`")
    sleep(2)
    await ayiin.edit("`๐๐๐๐จ๐ฉ ๐๐๐ฃ๐๐ข๐๐ก 10 ๐๐ง๐ช๐ฅ`")
    sleep(1)
    await ayiin.edit("`๐๐๐๐  ๐๐จ, ๐ฟ๐๐ฃ ๐๐จ ๐ฝ๐ช๐ ๐ฉ๐ ๐๐๐๐จ๐ฉ`")


@ayiin_cmd(pattern="uno(?: |$)(.*)")
async def _(uno):
    xd = await edit_or_reply(uno, "`๐๐๐ ๐ ๐  ๐๐`")
    sleep(2)
    await xd.edit("`๐ฝ๐๐ฌ๐๐ฃ ๐๐ฃ๐ค ๐ฎ๐ช๐  ๐`")
    sleep(1)
    await xd.edit("`๐๐๐ฃ๐ ๐๐๐ก๐๐ ๐๐๐ฃ๐๐๐ ๐ผ๐๐๐ข๐ ๐`")


CMD_HELP.update(
    {
        "gabut2": f"**Plugin : **`gabut2`\
        \n\n  ยป  **Perintah :** `{cmd}teemo`\
        \n  ยป  **Kegunaan : **Coba Sendiri Tod.\
        \n\n  ยป  **Perintah :** `{cmd}give`\
        \n  ยป  **Kegunaan : **Coba Sendiri Tod.\
        \n\n  ยป  **Perintah :** `{cmd}uno`\
        \n  ยป  **Kegunaan : **Coba Sendiri Tod.\
    "
    }
)
