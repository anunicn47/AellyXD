# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits
# Recode By : @AellyXD

from asyncio import sleep

from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsKicked

from AellyXD import CMD_HELP
from AellyXD import CMD_HANDLER as cmd
from AellyXD.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


@ayiin_cmd(pattern="banall(?: |$)(.*)")
async def testing(AellyXD):
    ayiin = await AellyXD.get_chat()
    yins = await AellyXD.client.get_me()
    admin = ayiin.admin_rights
    creator = ayiin.creator
    if not admin and not creator:
        await eod(AellyXD, get_string("stvc_1").format(yins.first_name))
        return
    xnxx = await eor(AellyXD, get_string("yiban_1"))
# Thank for Dark_Cobra
    ayiinkontol = await AellyXD.client.get_participants(AellyXD.chat_id)
    for user in ayiinkontol:
        if user.id == yins.id:
            pass
        try:
            xx = await AellyXD.client(EditBannedRequest(AellyXD.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await eod(xnxx, get_string("error_1").format(str(e)))
        await sleep(.5)
    await xnxx.edit(get_string("yiban_2"))


@ayiin_cmd(pattern="unbanall(?: |$)(.*)")
async def _(ayiin):
    yins = await eor(ayiin, get_string("yiban_3"))
    p = 0
    (await ayiin.get_chat()).title
    async for i in ayiin.client.iter_participants(
        ayiin.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await ayiin.client.edit_permissions(ayiin.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await yins.edit(get_string("yiban_4").format(p))


CMD_HELP.update(
    {
        "yinsban": f"**Plugin : **`yinsban`\
        \n\n  »  **Perintah :** `{cmd}banall`\
        \n  »  **Kegunaan :** Banned Semua Member Dalam Satu Ketikan.\
        \n\n  »  **Perintah :** `{cmd}unbanall`\
        \n  »  **Kegunaan :** Membatalkan Banned Anggota Group.\
    "
    }
)
