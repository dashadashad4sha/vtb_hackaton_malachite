import telebot
from telebot import types
# from ipynb.fs.defs.ml import is_user_alive

# привет, ты кто? (выбор из 2, еще надо масштабировать роли)
# Что тебе нужно, новости или инсайды
# я hr (выбирает и ему дается 3 подходящие новости)

bot = telebot.TeleBot('5741922635:AAG-R4CkgTqc9qGdl5bxRm64Jz0tDs7ql9E')

roles = ['Гендир', 'Бухгалтер']
choices_in_code = ['Новости', 'Инсайты и тренды']

# roles для каждой роли линамически

roles_in_code = [f'Я {role}' for role in roles]


choice = ''
role = ''


def create_button(name_and_text: str):
    name_and_text = types.KeyboardButton(name_and_text)
    return name_and_text


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for choice in choices_in_code:
        markup.add(create_button(choice))
    bot.send_message(message.chat.id, 'Привет, что тебе нужно, инсайды или новости?', reply_markup=markup)
    bot.register_next_step_handler(message, check_choice)


def check_choice(message):
    global choice
    choice = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for role in roles_in_code:
        markup.add(create_button(role))
    bot.send_message(message.from_user.id, 'Хорошо, какая у вас роль?', reply_markup=markup)
    bot.register_next_step_handler(message, message_reply)


# def get_news(message):


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for role in roles_in_code:
#         markup.add(create_button(role))
#     bot.send_message(message.chat.id, 'Привет, ты кто?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    global choice
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/start")
    markup.add(item1)
    if message.text in roles_in_code:
        if choice in choices_in_code:
            bot.send_message(message.chat.id, f'{choice} для {message.text.removeprefix("Я ")}')
        bot.send_message(message.chat.id, 'Нажмите /start чтобы начать с начала', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /start для начала работы')


# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
#         .... #код сохранения данных, или их обработки
#         bot.send_message(call.message.chat.id, 'Запомню : )');
#     elif call.data == "no":
#          ... #переспрашиваем


if __name__ == '__main__':
    print('Start bot')
    while True:
        bot.infinity_polling()
