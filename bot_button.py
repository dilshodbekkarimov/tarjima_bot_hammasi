from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from main import *



# bosh menu bu bo'limlarni tanlash uvhun button

bosh_menu = InlineKeyboardMarkup(
	inline_keyboard = [

	            	[
	            		KeyboardButton(text="Jahon tillari()",callback_data='jahon_tillari')
	            	],
		            [
	            		KeyboardButton(text="MDH Tillari() ",callback_data='mdh')
	            	],
	            	[
	            		KeyboardButton(text="Dunyo tillari()",callback_data='dunyo')
	            	],

				],
					
)


## xalqaro 6 til ucun button

jahon_tillari = types.InlineKeyboardMarkup()
jn_1 = types.InlineKeyboardMarkup(text="🇮🇳 hindi",callback_data="hi")
jn_2 = types.InlineKeyboardMarkup(text="🇬🇧 english ",callback_data="en")
jn_3 = types.InlineKeyboardMarkup(text="🇷🇺 русский",callback_data="ru")
jn_4 = types.InlineKeyboardMarkup(text="🇪🇸 spanish",callback_data="es")
jn_5 = types.InlineKeyboardMarkup(text="🇩🇪 german",callback_data="de")
jn_6 = types.InlineKeyboardMarkup(text="🇸🇦 عربي",callback_data="ar")
jn_7 = types.InlineKeyboardMarkup(text="🇨🇳 chinese (traditional)",callback_data="zh-tw")
knopka_101 = types.InlineKeyboardMarkup(text="🗑Tozalash/cleang/уборка",callback_data="tozala")
jahon_tillari.add(jn_1,jn_2,jn_3,jn_4,jn_5,jn_6,jn_7,knopka_101)



# mustaqil davlatlar hamdo'stligi davlatlari tili va dunyoning boshqa 100 davlatining tili ham shunday yoziladi.
### eslatma buttonlar 100 tadan ko'p bo'lolmaydi