# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot

import asyncio
from datetime import datetime
from io import BytesIO

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import Channel

import AellyXD.modules.sql_helper.gban_sql as gban_sql
from AellyXD import BOTLOG_CHATID
from AellyXD import CMD_HANDLER as cmd
from AellyXD import CMD_HELP, DEVS, WHITELIST, blacklistayiin
from AellyXD.events import register
from AellyXD.ayiin import ayiin_cmd, chataction, edit_or_reply, get_user_from_event
from Stringyins import get_string

from .admin import BANNED_RIGHTS, UNBAN_RIGHTS


async def admin_groups(grp):
    admgroups = []
    async for dialog in grp.client.iter_dialogs():
        entity = dialog.entity
        if (
            isinstance(entity, Channel)
            and entity.megagroup
            and (entity.creator or entity.admin_rights)
        ):
            admgroups.append(entity.id)
    return admgroups


def mentionuser(name, userid):
    return f"[{name}](tg://user?id={userid})"


@ayiin_cmd(pattern="gban(?: |$)(.*)")
@register(pattern=r"^\.cgban(?: |$)(.*)", sudo=True)
async def gban(event):
    if event.fwd_from:
        return
    sender = await event.get_sender()
    me = await event.client.get_me()
    if sender.id != me.id:
        gbun = await event.reply(get_string("gban_2"))
    else:
        gbun = await edit_or_reply(event, get_string("gban_2"))
    start = datetime.now()
    user, reason = await get_user_from_event(event, gbun)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await gbun.edit("**ππππ₯πππ£ πππππππ£ πΏππ§π πππ£πππ§π ππ€ππ‘π€π  π½**")
        return
    if user.id in DEVS:
        await gbun.edit(get_string("gban_5"))
        return
    if user.id in WHITELIST:
        await gbun.edit(get_string("gban_6"))
        return
    if gban_sql.is_gbanned(user.id):
        await gbun.edit(
            f"**ππ** [πππ’ππ©](tg://user?id={user.id}) **ππ£π ππͺπππ πΌππ πΏπ πΏπππ©ππ§ ππ½ππ£π£ππ**"
        )
    else:
        gban_sql.freakgban(user.id, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await gbun.edit("**πΌπ£ππ πππππ  πππ’π₯πͺπ£π?ππ ππ πππ£π πΌπ£ππ πΌππ’ππ£ π₯Ί**")
        return
    await gbun.edit(
        f"**ππ£ππ©πππ©ππ£π ππππ£ ππ πππ** [πππ’ππ©](tg://user?id={user.id}) **ππ£** `{len(san)}` **ππ§π€πͺπ₯π¨**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**πΌπ£ππ πππππ  πππ’ππ‘ππ π ππ―ππ£ π½ππ£π£ππ πΏπ :**\n**ππ§π€πͺπ₯ πΎπππ© :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await gbun.edit(
            f"**\\#ππ½ππ£π£ππ_ππ¨ππ§//**\n\n**πππ§π¨π© πππ’π :** [{user.first_name}](tg://user?id={user.id})\n**ππ¨ππ§ ππΏ :** `{user.id}`\n**πΌππ©ππ€π£ : ππ½ππ£π£ππ ππ£ {count} ππ§π€πͺπ₯π¨**\n**πΏπͺπ§ππ©ππ€π£ ππππ£π£ππ :** `{timetaken}` **ππππ€π£ππ¨**!!\n**ππππ¨π€π£ :** `{reason}`\n**ππ€π¬ππ§ππ π½π? : β§ π°ππΈπΈπ½-πππ΄ππ±πΎπ β§**"
        )
    else:
        await gbun.edit(
            f"**\\#ππ½ππ£π£ππ_ππ¨ππ§//**\n\n**πππ§π¨π© πππ’π :** [{user.first_name}](tg://user?id={user.id})\n**ππ¨ππ§ ππΏ :** `{user.id}`\n**πΌππ©ππ€π£ : ππ½ππ£π£ππ ππ£ {count} ππ§π€πͺπ₯π¨**\n**πΏπͺπ§ππ©ππ€π£ ππππ£π£ππ :** `{timetaken}` **ππππ€π£ππ¨**!!\n**ππ€π¬ππ§ππ π½π? : β§ π°ππΈπΈπ½-πππ΄ππ±πΎπ β§**"
        )


@ayiin_cmd(pattern="ungban(?: |$)(.*)")
@register(pattern=r"^\.cungban(?: |$)(.*)", sudo=True)
async def ungban(event):
    if event.fwd_from:
        return
    sender = await event.get_sender()
    me = await event.client.get_me()
    if sender.id != me.id:
        ungbun = await event.reply("`ππ£ππππ£π£ππ£π...`")
    else:
        ungbun = await edit_or_reply(event, "`ππ£ππππ£π£ππ£π...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, ungbun)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.freakungban(user.id)
    else:
        await ungbun.edit(
            f"**ππ** [πππ’ππ©](tg://user?id={user.id}) **ππ£π πππππ  πΌππ πΏππ‘ππ’ πΏπππ©ππ§ ππππ£ πΌπ£ππ**"
        )
        return
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await ungbun.edit("**πΌπ£ππ πππππ  πππ’π₯πͺπ£π?ππ ππ πππ£π πΌπ£ππ πΌππ’ππ£ π₯Ί**")
        return
    await ungbun.edit(
        f"**ππ£ππ©πππ©ππ£π ππ£ππππ£ ππ πππ** [πππ’ππ©](tg://user?id={user.id}) **ππ£** `{len(san)}` **ππ§π€πͺπ₯**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**πΌπ£ππ πππππ  πππ’ππ‘ππ π ππ―ππ£ π½ππ£π£ππ πΏπ :**\n**ππ§π€πͺπ₯ πΎπππ© :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await ungbun.edit(
            f"**ππ£ππππ£π£ππ** [{user.first_name}](tg://user?id={user.id}`) **ππ£** `{count}` **ππ§π€πͺπ₯π¨ ππ£** `{timetaken}` **ππππ€π£ππ¨**!!\n**ππππ¨π€π£ :** `{reason}`"
        )
    else:
        await ungbun.edit(
            f"**ππ£ππππ£π£ππ** [{user.first_name}](tg://user?id={user.id}) **ππ£** `{count}` **ππ§π€πͺπ₯π¨ ππ£** `{timetaken}` **ππππ€π£ππ¨**!!\n**πππ’π€π«ππ ππ§π€π’ ππππ£π‘ππ¨π©**"
        )


@ayiin_cmd(pattern="listgban$")
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "**πππ¨π© ππ‘π€πππ‘ π½ππ£π£ππ ππππ© ππ£π**\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"βοΈοΈοΈ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) **ππππ¨π€π£** `{a_user.reason}`\n"
            else:
                GBANNED_LIST += (
                    f"βοΈοΈοΈ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) `No Reason`\n"
                )
    if len(gbanned_users) >= 4096:
        with BytesIO(str.encode(GBANNED_LIST)) as fileuser:
            fileuser.name = "list-gban.txt"
            await event.client.send_file(
                event.chat_id,
                fileuser,
                force_document=True,
                thumb="AellyXD/resources/logo.jpg",
                caption="**List Global Banned**",
                allow_cache=False,
            )
    else:
        GBANNED_LIST = "π½ππ‘πͺπ’ πΌππ πππ£πππͺπ£π πππ£π πΏπ-ππππ£"
    await edit_or_reply(event, GBANNED_LIST)


@chataction()
async def _(event):
    if event.user_joined or event.added_by:
        user = await event.get_user()
        chat = await event.get_chat()
        if gban_sql.is_gbanned(
                user.id) and blacklistayiin and chat.admin_rights:
            try:
                await event.client.edit_permissions(
                    chat.id,
                    user.id,
                    view_messages=False,
                )
                await event.reply(
                    f"**#ππππ£π£ππ_ππ¨ππ§** ππ€ππ£ππ.\n\n** β’ πππ§π¨π© πππ’π:** [{user.first_name}](tg://user?id={user.id})\n β’ **πΌππ©ππ€π£:** `Banned`"
                )
            except BaseException:
                pass


# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot


CMD_HELP.update(
    {
        "gban": f"**Plugin : **`gban`\
        \n\n  Β»  **Perintah :** `{cmd}gban` <username/id>\
        \n  Β»  **Kegunaan : **Melakukan Banned Secara Global Ke Semua Grup Dimana anda Sebagai Admin.\
        \n\n  Β»  **Perintah :** `{cmd}ungban` <username/id>\
        \n  Β»  **Kegunaan : **Membatalkan Global Banned\
        \n\n  Β»  **Perintah :** `{cmd}listgban`\
        \n  Β»  **Kegunaan : **Menampilkan List Global Banned\
    "
    }
)
