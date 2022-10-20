from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAFQ6LljGsrT4XPljp14SXutiGgdSWYaQgACegEAAhAabSKcnbdITu9y3ikE")
    await message.reply_text(
      f"""**{bot} Sizi Salamlayır👋🏻\n\nℹ️ Mən səsli söhbətlərdə musiqi oxuya bilən bir botam\n\n✅ Botun istifadə qaydasını öyrənmək üçün /help əmrindən istifadə edin\n\n🆘 Hər hansı problemlə qarşılaşsanız @UlviSup qrupumuza gəlib bildirə bilərsiniz!\n\n🎵 Musiqi yükləmək üçün digər botumuz: @UlviSongRobot\n\n🤖 Digər Botlar: @UlviProject**
      """,
         reply_markup
         =InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Məni öz qrupuna əlavə et ➕", url=f"https://t.me/Ulvi_Music_Bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧔🏻 Sahibim", url="https://t.me/BrendUlvi"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿 Rəsmi Kanal", url="https://t.me/UlviProject"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💡 Əmrlər" , callback_data= "cbhelp"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]))
async def help(_, message: Message):
      await message.reply_text(" Səsli söhbətdə musiqi oxuması üçün /play əmrindən istifadə edə bilərsiniz ⤵️\n\nMəsələn:\n\n1. `/play Ayaz Babayev - Sən mənlə`\n2. `/play https://youtu.be/qLXUa89Q5WI`\n\n/alive - Botun işlək olduğunu yoxlamaq üçün əmrdir. Yalnız bot sahibi istifadə edə bilər.\n\n⚠️ Botun qruplarda işləyə bilməsi üçün admin olmalıdır !", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "ℹ️ Bütün əmrlərim", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "✅ Məlumatlarım", callback_data="hərkəs")
                 ],[
                     InlineKeyboardButton(
                         "⬅️ Geri qayıt", callback_data="cbstart")
                 ]
             ]
         )
    )
    
    
@Client.on_callback_query(filters.regex("cbhelp"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" Səsli söhbətdə musiqi oxuması üçün /play əmrindən istifadə edə bilərsiniz ⤵️\n\nMəsələn:\n\n1. `/play Ayaz Babayev - Sən mənlə`\n2. `/play https://youtu.be/qLXUa89Q5WI`\n\n/alive - Botun işlək olduğunu yoxlamaq üçün əmrdir. Yalnız bot sahibi istifadə edə bilər.\n\n⚠️ Botun qruplarda işləyə bilməsi üçün admin olmalıdır !", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "ℹ️ Bütün əmrlərim", callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "✅ Məlumatlarım",callback_data ="hərkəs")
        ],
        [
          InlineKeyboardButton(
            "⬅️ Geri qayıt", callback_data="cbstart")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("hərkəs"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Hələ hazır deyiləm😁</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri qayıt", callback_data="cbhelp")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}! Bu botun hərkəs üçün əmr menyusu 🙂\n\n/play - Musiqi oxutmaq üçün youtube url'sinə vəya musiqi dosyasına yanıt verin ▶️\n/song - İstədiyiniz musiqi sürətli bir şəkildə axtarın 🎵\n/vsong - İstədiyiniz videoları sürətli bir şəkildə axtarın 🔍\n\nBu botun adminlər üçün əmr menyusu ✅\n\n/pause - Musiqini dayandır ⏸️\n/resume - Musiqini dəvam etdir ▶️\n/end - Musiqini bitir ⏹\n/skip - Musiqini keçin ⏩\n/ses - Səsi 0-200 arası dəyiş\n/reload - Botu yenidən başlat 🔄\n/asistan - Musiqi asistanı qrupunuza qoşulur ⚪\n\nSahiblər və sudo üçün əmirlər menyusu\n\n/yetkiver - Bir istifadəçiyə yetki ver 🔼\n/yetkial - İstifadəçinin yetkisin al 🔽\n/reklam - Bot olduğu bütün qruplarda reklam edər 📢\n/restart - Botu serverdən yenidən başladın 🔃\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "️⬅️ Geri qayıt", callback_data="cbhelp")
                     ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**{bot} Sizi Salamlayır👋🏻\n\nℹ️ Mən səsli söhbətlərdə musiqi oxuya bilən bir botam\n\n✅ Botun istifadə qaydasını öyrənmək üçün /help əmrindən istifadə edin\n\n🆘 Hər hansı problemlə qarşılaşsanız @UlviSup qrupumuza gəlib bildirə bilərsiniz!\n\n🎵 Musiqi yükləmək üçün digər botumuz: @UlviSongRobot\n\n🤖 Digər Botlar: @UlviProject**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Məni öz qrupuna əlavə et ➕", url=f"https://t.me/Ulvi_Music_Bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧔🏻 Sahibim", url="https://t.me/BrendUlvi"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿 Rəsmi Kanal", url="https://t.me/UlviProject"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💡 Əmrlər", callback_data= "cbhelp"
                    )
                ]
                
           ]
        ),
    )
