# Ayiin - Userbot
# Copyright (C) 2022-2023 @AellyXD
#
# This file is a part of < https://github.com/AellyXD/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AellyXD/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AellyXD/Ayiin-Userbot>
# t.me/AellyXDSupport & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from time import sleep
from secrets import choice

from AellyXD import CMD_HANDLER as cmd
from AellyXD import CMD_HELP
from AellyXD.ayiin.truthdare import Dare as d
from AellyXD.ayiin.truthdare import Truth as t
from AellyXD.ayiin import ayiin_cmd, eor
from Stringyins import get_string


Tod = ["Truth", "Dare"]


@ayiin_cmd(pattern=r"tod( truth| dare|$)")
async def truth_or_dare(tord):
    trod = tord.pattern_match.group(1).strip()
    troll = choice(Tod)
    if trod == "":
        await tord.edit(get_string("tod_1").format(troll))

    if trod == "truth":
        Ayiin = await eor(tord, get_string("tod_2"))
        sleep(1)
        trth = choice(t)
        await Ayiin.edit(get_string("tod_3").format(trth))
        return

    if trod == "dare":
        Xd = await eor(tord, get_string("tod_4"))
        sleep(1)
        dr = choice(d)
        await Xd.edit(get_string("tod_5").format(dr))

        return


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinstod": f"**Plugin:** `yinstod`\
        \n\n  »  **Perintah :** `{cmd}tod`\
        \n  »  **Kegunaan :** __Mendapatkan Pilihan Secara Acak.__\
        \n\n  »  **Perintah :** `{cmd}tod <truth/dare>`\
        \n  »  **Kegunaan :** __Untuk Mendapatkan Truth or Dare Secara Acak.__\
    "
    }
)
