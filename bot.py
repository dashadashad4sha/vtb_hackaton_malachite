import telebot
from telebot import types
import random
import schedule
from functools import wraps
from parser.parsing import start_parse
# from ipynb.fs.defs.ml import is_user_alive

bot = telebot.TeleBot('5741922635:AAG-R4CkgTqc9qGdl5bxRm64Jz0tDs7ql9E')

insides = {
    'Пандемия коронавируса заставила людей внимательней относиться к своему здоровью.': 'Большим спросом пользуются тест-системы для определения вирусных заболеваний в домашних условиях.',
    'Банк России представил свою «оптимальную стратегию регулирования криптовалют: регулятор планирует запретить майнинг, выпуск, обращение и обмен криптовалют, в том числе биткойна, любыми российскими игроками и криптобиржами.': 'Это приведёт к миграции участников рынка за рубеж.',
    'Россия лидирует по числу наложенных санкций.': 'Растёт спрос на внутренний туризм',
    'На фоне эскалации конфликта с Украиной в России объявлена частичная мобилизация.': 'Растёт количество поисковых запросов на бронежилеты',
    'В России закрыты южные аэропорты.': 'Это ведёт к росту популярности железнодорожных и автомобильных перевозок.',
    }
# для работы кнопок и логики, также тут можно добавлять роли
roles = ['Гендир', 'Бухгалтер']
choices_in_code = ['Новости', 'Инсайты и тренды']
# roles для каждой роли линамически
roles_in_code = [f'Я {role}' for role in roles]

choice = ''
role = ''


# остановка бота и сбор новых новостей
def new_parsing():
    bot.stop_polling()
    start_parse()


# остановка бота каждый день в 3 часа
schedule.every().day.at("02:47").do(new_parsing)

# def mult_threading(func):
#     """Декоратор для запуска функции в отдельном потоке"""
#
#     @wraps(func)
#     def wrapper(*args_, **kwargs_):
#         import threading
#         func_thread = threading.Thread(target=func,
#                                        args=tuple(args_),
#                                        kwargs=kwargs_)
#         func_thread.start()
#         return func_thread
#
#     return wrapper


def create_button(name_and_text: str):
    name_and_text = types.KeyboardButton(name_and_text)
    return name_and_text


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for choice in choices_in_code:
        markup.add(create_button(choice))
    bot.send_message(message.from_user.id, 'Привет, что тебе нужно, инсайты или новости?', reply_markup=markup)
    bot.register_next_step_handler(message, check_choice)


def check_choice(message):
    global choice
    choice = message.text
    if choice == "Инсайты и тренды":
        get_insides(message)
        # bot.register_next_step_handler(message, get_insides)
    if choice == "Новости":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for role in roles_in_code:
            markup.add(create_button(role))
        bot.send_message(message.from_user.id, 'Хорошо, какая у вас роль?', reply_markup=markup)
        bot.register_next_step_handler(message, message_reply)


def get_insides(message):

    for key in random.sample(list(insides), 3):
        text = f'Тренд - {key}\nИнсайт - {insides[key]}'
        bot.send_message(message.from_user.id, text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/start")
    markup.add(item1)
    bot.send_message(message.from_user.id, 'Нажмите /start чтобы начать с начала', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    global choice
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/start")
    markup.add(item1)
    if message.text in roles_in_code:
        if choice in choices_in_code:
            bot.send_message(message.from_user.id, f'{choice} для {message.text.removeprefix("Я ")}')
        bot.send_message(message.from_user.id, 'Нажмите /start чтобы начать с начала', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /start для начала работы')


if __name__ == '__main__':
    print('Start bot')

    while True:
        schedule.run_pending()
        bot.polling()

