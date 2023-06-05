from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

button1 = KeyboardButton("Ro'yxatdan o'tish📌")
keyboard1 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button1)

button2 = InlineKeyboardButton(text='Android uchun📱',callback_data='android')
button3 = InlineKeyboardButton(text='IOS uchun🎛',callback_data='ios')
keyboard2 = InlineKeyboardMarkup().add(button2,button3)


button4 = KeyboardButton('Samarqand shahar')
button5 = KeyboardButton('Samarqand tuman')
button6 = KeyboardButton("Bulung'ur tumani")
button7 = KeyboardButton("Jomboy tumani")
button8 = KeyboardButton('Ishtixon tumani')
button9 = KeyboardButton("Kattaqo'rg'on tumani")
button10 = KeyboardButton("Kattaqo'rg'on shahar")
button11 = KeyboardButton('Toyloq tumani')
button12 = KeyboardButton("Qo'shrabot tumani")
keyboard3 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button4,button5).row(button6,button7).row(button8,button9).row(button10,button11).row(button12)

button13 = KeyboardButton("Tasdiqlash✅")
button14 = KeyboardButton("Qaytadan o'tish🔄")
keyboard4 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).add(button13).add(button14)


button15 = KeyboardButton("Info👤")
keyboard5 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).add(button15)