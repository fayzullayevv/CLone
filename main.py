from aiogram import Bot,types,Dispatcher,executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from buttons import *
from text import *
from index import *

API_TOKEN = '5831598621:AAEQSUWdaTLzyQLIMPnT3gPaNRBnnCd59KY'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

users = {}

@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    if message.from_user.id not in users:
        await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! {salomlashish}",reply_markup=keyboard1)
        await message.answer("Ro'yhatdan o'tish uchun pastdagi tugmani bosing👇👇")
    else:
        await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! {salomlashish}")
        await message.answer("Ro'yxatdan o'tgansiz!",reply_markup=keyboard5)


@dp.message_handler(text='Info👤')
async def info(message: types.Message):
  if message.from_user.id in users:
    data = users[message.from_user.id]
    info_message = f"""
    Sizning shaxsiy ma'lumotlaringiz:

👤 Ism: {data['name']}
👥 Familiya: {data['last_name']}
📞 Telefon: {data['number']}
🏫 Maktab: {data['school']}
📍 Hudud: {data['location']}
    """
    await message.answer(info_message)
  else:
    await message.answer("Siz hali registratsiyadan o'tmadingiz!",reply_markup=keyboard1)


@dp.message_handler(content_types='text')
async def text(message:types.Message):
    # Ro'yhatdan utish
    state = dp.current_state(user=message.from_user.id)
    if message.from_user.username is None:
        await message.answer("Ro'yhatdan o'tish uchun sizda telegram username mavjud emas! Iltimos, username kiriting!\n \nQo'llanma uchun video tanlang!",reply_markup=keyboard2)
    if message.from_user.username is not None:
        if message.text == "Ro'yxatdan o'tish📌" and message.from_user.id not in users:
            await message.answer('Iltimos, ismingizni kiriting!\n(Masalan: Anvar)')
            await state.set_state(Register.name)
 
@dp.message_handler(state=Register.name)
async def get_name(message:types.Message,state:FSMContext):
    name = message.text
    if len(name)>=5 or '.' not in name or '_' not in name or name==str:
      await state.update_data({'name':name})
      await message.answer('Iltimos familiyangizni kiriting!\n(Masalan: Rasulov)')
      await Register.next()
    else:
       await message.answer("Iltimos ismigizni to'g'ri kiriting! \n(Masalan:Anvar)")

@dp.message_handler(state=Register.last_name)
async def get_last_name(message:types.Message,state:FSMContext):
    last_name = message.text
    if last_name[-2::]=='ov' or last_name[-2::]=='ev' or last_name[-2::]=='va' or last_name==str:
      await state.update_data({'last_name':last_name})
      await message.answer('Iltimos telefon raqamingizni kiriting!\n(Masalan: 998950127733)')
      await Register.next()
    else:
      await message.answer("Itimos familyangizni to'g'ri kiriting!\n(Masalan:Rasulov)")

@dp.message_handler(state=Register.number)
async def get_number(message:types.Message,state:FSMContext):
    number = message.text
    if len(number)<12 or number==str or str(number)[0:4]=='998' or len(number)>12:
      await message.answer("Iltimos telefon raqamingizni to'g'ri kiriting!\n(Masalan:998950127733)")
    elif len(number)==12:
      await state.update_data({'number':number})
      await message.answer('Iltimos hududingizni tanlang!',reply_markup=keyboard3)
      await Register.next()

@dp.message_handler(state=Register.location)
async def get_location(message:types.Message,state:FSMContext):
    location = message.text
    await state.update_data({'location':location})
    await message.answer("Iltimos o'qigan maktabingizni kiriting!\n(Masalan: 1-maktab yoki 1-IDUM)")
    await Register.next()

@dp.message_handler(state=Register.school)
async def get_school(message:types.Message,state:FSMContext):
    school = message.text
    if 'maktab' in school or 'IDUM' in school:
      await state.update_data({'school':school})
      data = await state.get_data()
      await message.answer(f"{tekshirish} \n👤 Ism: {data['name']}\n👥 Familiya: {data['last_name']}\n📞 Telefon: {data['number']}\n🏫 Maktab: {data['school']}\n📍 Hudud: {data['location']} \n\n✅ Tasdiqlash tugmasini bosing!\n\n ❗️Ma'lumotlarinigiz xato kiritilgan bo'lsa 🔄 Qayta o'tish tugmasini bosing!",reply_markup=keyboard4)
      await Register.next()
    else:
       await message.answer("Iltimos, o'qigan maktabingizni to'g'ri kiriting!\n(Masalan: 1-maktab yoki 1-IDUM)")



@dp.message_handler(state=Register.cheeck)  
async def get_cheeck(message:types.Message,state:FSMContext):
    user = message.from_user.id
    cheeck = message.text
    await state.update_data({'cheeck':cheeck})
    if cheeck == "Tasdiqlash✅":
      await message.answer("Siz muvaffaqiyatli ro'yxatdan o'tdingiz!",reply_markup=keyboard5)
      data = await state.get_data()
      users[message.from_user.id] = data
      await state.finish()
      print(user)
    elif cheeck == "Qaytadan o'tish🔄":
          await message.answer('Iltimos, ismingizni kiriting!\n(Masalan: Anvar)')
          await Register.name.set()


@dp.callback_query_handler(text=['android','ios'])
async def qollanma(call:types.CallbackQuery):
    if call.data == 'android':
        video = open('video/android.mp4','rb')
        await bot.send_video(chat_id=call.from_user.id,video=video,caption="username kiritib bo'lgach 'Ro'yxatdan o'tish!' tugmasini qayta kriting!")
    if call.data == 'ios':
        video = open('video/ios.mp4','rb')
        await bot.send_video(chat_id=call.from_user.id,video=video,caption="username kiritib bo'lgach 'Ro'yxatdan o'tish!' tugmasini qayta kriting!")


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)