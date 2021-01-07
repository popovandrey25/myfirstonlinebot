# Подключаем библиотеку случайных чисел 
import random

# Подключаем библиотеку для Телеграма
import telebot

# Импортируем типы из библиотеки, чтобы создавать кнопки
from telebot import types

# Указываем токен
bot = telebot.TeleBot('1517274151:AAHPb3WzTkj6bXFzB_DjkGOPxj5-85l2uzo')

# Список группы
list = [
    "Абаровский Олег Александрович", "Абдуль Хади Филипп Ибрахим",
    "Алапанова Эльза Халилевна", "Апанович Денис Станиславович",
    "Бахарев Владимир Денисович", "Варламова Анна Борисовна",
    "Волошинская Евгения Владимировна", "Гапонов Никита Алексеевич",
    "Казаков Илья Владимирович", "Камальдинов Ильдар Рустамович",
    "Капичников Ярослав Андреевич", "Куценко Борис Дмитриевич",
    "Макаров Глеб Александрович", "Мерц Савелий Павлович",
    "Михеева Кристина Олеговна", "Недосекин Максим Александрович",
    "Павлов Артем Андреевич", "Пономарев Никита Владимирович",
    "Попов Андрей Викторович", "Сафонникова Анна Романовна",
    "Соколов Даниил Витальевич", "Степанов Данила Михайлович",
    "Сысоев Максим Алексеевич", "Тихонов Федор Андреевич",
    "Чекменев Вячеслав Алексеевич", "Шар Алексей Михайлович"
]

present_list = list.copy()

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
    # Если написали
    if message.text == "/start":
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик
        key_present = types.InlineKeyboardButton(text = 'Список в случайном порядке', callback_data = 'present_list')
        # И добавляем кнопку на экран
        keyboard.add(key_present)
        key_list = types.InlineKeyboardButton(text = 'Список группы', callback_data = 'list')
        keyboard.add(key_list)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text = 'Нажмите кнопку.', reply_markup = keyboard)
    elif message.text == "/random":
        random.shuffle(present_list)
        bot.send_message(message.from_user.id, "Список обновлен.")
    else:
        bot.send_message(message.from_user.id, "Напишите /start.")

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func = lambda call: True)
def callback_worker(call):
    if call.data == "present_list":
        msg = 'Список:'
        for i in range(26):
            msg = msg + '\n' + present_list[i]
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "list":
        msg = 'Список:'
        for i in range(26):
            msg = msg + '\n' + list[i]
        bot.send_message(call.message.chat.id, msg)

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop = True, interval = 0)