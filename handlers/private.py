from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**ð·ï¸ Há´Ê, Éª á´á´ [ð ððð¶ð° ð¡ð²ðð ð](https://telegra.ph/file/89d4135199d1d2a98596e.jpg).
á´É´ á´á´á´ á´É´á´á´á´ á´Êá´á´Éªá´á´ sá´á´á´Ê
Òá´sá´ É´á´xá´ É¢á´É´á´Êá´á´Éªá´É´ á´á´sÉªá´
á´Êá´Êá´Ê Êá´á´..!
âââââââââââââââââââ
â£â Êá´É´ á´É´ á´ÊÉªá´ á´á´á´ á´ á´ê± ê±á´Ê. 
â£â ÊÉªÉ¢Ê Ç«á´á´ÊÉªá´Ê á´á´ê±Éªá´.
â£â É´á´ Êá´É¢ ÉªÉ´ ÉªÉ´ á´ á´Éªá´á´.
â£â ê±á´á´á´Êê°á´ê±á´ ê±á´á´á´á´.
âââââââââââââââââââ
 á´Êá´á´á´á´á´ ÊÊ : [á´Êá´á´á´á´Ê á´á´á´ á´É´](https://t.me/Pavanmagar)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð½ ð¥ðð£ð¢", url="https://t.me/CreatorPavanRepo"
                    ),
                    InlineKeyboardButton(
                        "ðð¢ð¦ð¦ ð", url="https://t.me/Pavanmagar")
                ],[ 
                    InlineKeyboardButton(
                        "ð ððð ð ð ð", url="https://t.me/CrepanRobot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ð ððð¶ð° ðð¼ð ð¢ð»ð¹ð¶ð»ð² ð¡ð¼ð\nð ðð²ðð¼ð¿ ð«ð <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¼ð¦ðð½ð½ð¼ð¿ð", url="https://t.me/Prayagraj_Op")
                ]
            ]
        )
   )
