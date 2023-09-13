###### BISMILLAH
from googletrans import Translator #tarjima uchun  cmdga "pip install googletrans" buyrug'ini bering
import logging
from bot_token import admin,token # admin idisi va tokenni boshqa filega saqlasak undan shunday chaqirib olamiz
from aiogram import Bot, Dispatcher, types,executor
from bot_button import *# b utton fileni chaqirib olamiz
from baza import * # baza fileni chqaririb olamiz

from aiogram.contrib.fsm_storage.memory import MemoryStorage  # vaqtinchalik xotra uchun 
from aiogram.dispatcher import FSMContext #state uchun 
from state import StateData


logging.basicConfig(level=logging.INFO)

bot = Bot(token=token) ####aynan shu yerga token yoki token uchun qo'yilgan o'zgaruvchi qo'yiladi# 
dp = Dispatcher(bot, storage=MemoryStorage())   # vaqtinchalik xotra uchun 

db = Database()

tr = Translator()   #tarjima uchun 



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    tel_id = message.from_user.id   #foydalanuvchi id sini chiqarib beradi 
    name = message.from_user.username #foydalanuvchi usernamwesini chiqarib beradi
    data = db.select_user_id(tel_id) 
    if data is None:
        db.insert_users(tel_id,name)
        await message.edit_photo(
        photo=open('images/fakt.jpg','rb'),
caption="""Assalomu Alaykum!👋\nXo'sh kelibsiz!🤝\nBu bot orqali siz o'ziningizning ma'lumotlaringizni 100 dan ortiq tillarga  tarjima qilolasiz.🤓🤓\n\n 🤝✅Mening boshqa loyhalarim;\n\t👨‍💻✅ @dilshodbeK_arimov kanalimda✅✅ \n👌✅ALBATTA OBUNA BO'LING \n\n \t🇺🇿 Marhamat so'z kiriting!!!""") ### agar foydalanuchi birinchi bor foydalanayotganda shunday javob beraddi 

    else:
    	await message.answer_photo(
        photo=open('images/fakt.jpg','rb'),
caption="""Assalomu Alaykum!👋🤝\n\n 🤝✅Mening boshqa loyhalarim;\n\t👨‍💻✅ @dilshodbeK_arimov kanalimda✅✅ \n👌✅ALBATTA OBUNA BO'LING \n\n\t🇺🇿 Marhamat so'z kiriting!!!""") # agar foydalanuvhi bazada bor bo'lsa shunday javob beradi,.

        
#buttonlarni bosh menudan tanlash orqali tillar ro'yxatini chiqara olasiz bu yerda 3 ta button bor

@dp.callback_query_handler(text="jahon_tillari")
async def knopka(call: types.CallbackQuery):
    await call.message.edit_text("""Assalomu alaykum!👋\nUshbu bo'limda xalqaro  tillar bor🤓🤓\n\n 🤝✅Mening boshqa loyhalarim;\n\t👨‍💻✅ @dilshodbeK_arimov kanalimda✅✅ \n👌✅ALBATTA OBUNA BO'LING """,reply_markup=jahon_tillari,)


@dp.callback_query_handler(text="mdh")
async def knopka(call: types.CallbackQuery):
    await call.message.edit_text("""Assalomu alaykum!👋\nUshbu bo'limda "MUSTAQIL DAVLATLAR HAMDO'SLIGI"ga a'zo davlatlarning tili bor🤓🤓\n\n 🤝✅Mening boshqa loyhalarim;\n\t👨‍💻✅ @dilshodbeK_arimov kanalimda✅✅ \n👌✅ALBATTA OBUNA BO'LING """,reply_markup=mdh_tillari,)



@dp.callback_query_handler(text="dunyo")
async def knopka(call: types.CallbackQuery):
    await call.message.edit_text("""Assalomu alaykum!👋\nUshbu bo'limda 100 ta eng ko'p ishlatiladigan  tillar bor🤓🤓\n\n 🤝Mening boshqa loyhalarim;\n\t👨‍💻✅ @dilshodbeK_arimov kanalimda✅✅ \n👌✅ALBATTA OBUNA BO'LING """,reply_markup=markup,)

########################++++++++++++++++++===============================================



###########################################################################
###################################################################################################################
#######################################################################3

# bu yerda tilni tanlash orqali tajima qiladi, quyidagilar textni global translation orqali tarjima qilishga yordam beradi, en/ uz / ru  kabi belgilar tilning rasmiy belgilari hisoblanib hamda buttonni ham ulab beradi.


@dp.message_handler()
async def echo(message: types.Message):
	await message.reply("👌✅Qoyilmaqom!👍\n👌✅Endi  tillardan birini tanlang!👍\n\n 🤝🤓Mening boshqa loyhalarim;\n\t👨‍💻✅ @dilshodbeK_arimov kanalimda✅✅ \n👌✅ALBATTA OBUNA BO'LING ",reply_markup=bosh_menu,)
	global msg 
	msg = message.text

@dp.callback_query_handler(text='uz')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='en')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='ru')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



    # aynan shu 3 til kabi 100lab tillarni ketma ket yozib chiqamiz.


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)