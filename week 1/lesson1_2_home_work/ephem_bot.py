"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

import ephem_bot_settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


def greet_user(bot, update): # функция приветствия
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.first_name, update.message.chat.id, update.message.text) #отображает данные пользователя, отправившего сообщение


def talk_to_me(bot, update): # функция зеркального ответа
    user_text = update.message.text 
    update.message.reply_text(f'Сам "{user_text}"')
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.first_name, update.message.chat.id, update.message.text) #отображает данные пользователя, отправившего сообщение

# функция вызывается при получении сбытия /planet
def get_constellation(bot, update):
    today = datetime.datetime.today().date() # получаю текущую дату и время, обрезаю до даты только

    user_text = update.message.text.split(" ") # забираю полное пользовательское сообщение, содержащее команду и кладу его в список по словам
    for item in user_text: # прохожу по каждому слову, чтобы обрабатывать запрос по нескольким планетам

        if item.lower() == '/planet': # саму команду пропускаю
            continue
        elif item.lower() == 'mars': # Марс
            mars = ephem.Mars(today)
            const = ephem.constellation(mars)
            update.message.reply_text(f'Сейчас: {today}, планета: {item.capitalize()}, созвездие: {const[1]}') # вывожу данные пользователю в чат с ботом
        elif item.lower() == 'moon': # Луна
            moon = ephem.Moon('1988/12/16')
            const = ephem.constellation(moon)
            update.message.reply_text(f'Сейчас: {today}, планета: {item.capitalize()}, созвездие: {const[1]}')
        elif item.lower() == 'saturn': # Сатурн
            saturn = ephem.Saturn('1988/12/16')
            const = ephem.constellation(saturn)
            update.message.reply_text(f'Сейчас: {today}, планета: {item.capitalize()}, созвездие: {const[1]}')
        elif item.lower() == 'jupiter': # Юпитер
            jupiter = ephem.Jupiter('1988/12/16')
            const = ephem.constellation(jupiter)
            update.message.reply_text(f'Сейчас: {today}, планета: {item.capitalize()}, созвездие: {const[1]}')
        # может есть еще планеты, но в документации в явном виде ничего не нашла, даже в списке звезд нет Солнца, очень странно.
        # а незнакомые названия звезд обрабатывать не стала


def main(): # основная функция
    mybot = Updater(ephem_bot_settings.API_KEY, request_kwargs=ephem_bot_settings.PROXY)

    logging.info('Bot is starting...')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", get_constellation)) # добавила обработчик новой (добавленной в бот в телеграме) команды, при получении которой вызываю функцию
    
    mybot.start_polling() # запуск мониторинга событий создания новых сообщений
    mybot.idle() # команда боту работать вплоть до принудительной остановки
       

if __name__ == "__main__":
    main()
