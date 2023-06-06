import telebot
from config import token
from parser import temp_weather
from parser import temp_weather_1
import random
from random import choice
bot = telebot.TeleBot(token)



def keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_weather = telebot.types.KeyboardButton('Погода')
    btn_pictures = telebot.types.KeyboardButton('Фотки')
    btn_quotes = telebot.types.KeyboardButton('цитаты')
    return keyboard.add(btn_weather, btn_pictures, btn_quotes)

def weather_keyboard():
    weather_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_weather_ekt = telebot.types.KeyboardButton('Екатеринбург')
    btn_weather_mlg = telebot.types.KeyboardButton('Малгобек')
    btn_back = telebot.types.KeyboardButton('Назад')
    return weather_keyboard.add(btn_weather_ekt, btn_weather_mlg, btn_back)

def pictures_keyboard():
    pictures_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_ilez = telebot.types.KeyboardButton('илез')
    btn_ibragim = telebot.types.KeyboardButton('ибрагим')
    btn_ahmed = telebot.types.KeyboardButton('ахмед')
    btn_back = telebot.types.KeyboardButton('назад')
    return pictures_keyboard.add(btn_ilez, btn_ahmed, btn_ibragim, btn_back)

quotes = ['банан', 'апельсин']

def quote_keyboard():
    quote_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_random = telebot.types.KeyboardButton('дайте цитату')
    return quote_keyboard.add(btn_random)


@bot.message_handler(commands=['start'])
def greeting(message):
    bot.send_message(message.from_user.id, 'Добро пожаловать в бота.\nВоспользуйтесь клавиатурой.', reply_markup = keyboard())
    bot.register_next_step_handler(message, switcher)

def weather_switcher(message):
    bot.send_message(message.from_user.id, 'Выберите город.', reply_markup=weather_keyboard())
    bot.register_next_step_handler(message, switcher_weather)

def switcher_weather(message):
    if message.text.lower() == 'екатеринбург':
        weather_ekt(message)
    elif message.text.lower() == 'малгобек':
        weather_mlg(message)
    elif message.text.lower() == 'назад':
        weather_back(message)


def weather_mlg(message):
    bot.send_message(message.from_user.id, f'На улице:\n{temp_weather_1}')
    bot.register_next_step_handler(message, switcher_weather)

def weather_ekt(message):
    bot.send_message(message.from_user.id, f'На улице:\n{temp_weather}')
    bot.register_next_step_handler(message, switcher_weather)



def switcher(message):
    if message.text.lower() == 'погода':
        weather_switcher(message)
    if message.text.lower() == 'фотки':
        pictures_switcher(message)
    if message.text.lower() == 'цитаты':
        quote_switcher(message)

def quote_1(message, quotes):
    bot.send_message(message.from_user.id, random.choice(quotes))
    switcher_quote(message)

def switcher_quote(message):
    if message.text.lower() == 'дайте цитату':
        quote_1(message)

def quote_switcher(message):
    bot.send_message(message.from_user.id, 'Жмите на угад, какая цитата выпадет, той вы и должны руководствоваться сегодня',
                     reply_markup=quote_keyboard())
    bot.register_next_step_handler(message, switcher_quote)


def weather_back(message):
    bot.send_message(message.from_user.id,'Выберите нужную команду:', reply_markup=keyboard())
    bot.register_next_step_handler(message, switcher)

def pictures_switcher(message):
    bot.send_message(message.from_user.id, 'Выберите человека.', reply_markup=pictures_keyboard())
    bot.register_next_step_handler(message, funny_pictures)

def funny_pictures(message):
    if message.text.lower() == 'илез':
        picture_ilez(message)
    elif message.text.lower() == 'ибрагим':
        picture_ibragim(message)
    elif message.text.lower() == 'ахмед':
        picture_ahmed(message)
    elif message.text.lower() == 'назад':
        weather_back(message)

def picture_ilez(message):
    bot.send_photo(message.from_user.id,
photo='https://sun9-64.userapi.com/impg/-JFlWKpheYp6NIU-1jI5WitJmLOMv8Hn1AXaLw/qbTYGn23a2M.jpg?size=808x1080&quality=96&sign=4e99f4e532360fb1d7702cdb1a9b483e&type=album')
    bot.register_next_step_handler(message, funny_pictures)


def picture_ibragim(message):
    bot.send_photo(message.from_user.id,
                   photo='https://sun9-32.userapi.com/impg/IYLENPGv_LH5oyFhCi1FhQ24eqOKwJZYkue8rA/cMmN7zARuFI.jpg?size=248x314&quality=96&sign=600987f32a0c5d865f2b17b08bc9b0ca&type=album')
    bot.register_next_step_handler(message, funny_pictures)


def picture_ahmed(message):
    bot.send_photo(message.from_user.id,
                   photo='https://sun3-17.userapi.com/impg/rzqxyRLfFYdb5Q-v-bNv0HsHrSFbAWEY7TOLog/PcC2vtFqxgQ.jpg?size=381x659&quality=96&sign=0b35c5c9e3c5cef0c2072f747aacc69f&type=album')
    bot.register_next_step_handler(message, funny_pictures)




bot.infinity_polling()


