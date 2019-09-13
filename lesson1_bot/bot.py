from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    logging.info('Call \start')
    update.message.reply_text("Привет от Ани!")


def talk_to_me(bot,update):
    user_text = f'Привет, {update.message.chat.first_name}! Ты написал: {update.message.text}' 
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.first_name, update.message.chat.id, update.message.text) #отображает данные пользователя, отправившего сообщение
    update.message.reply_text(user_text) # эхо-бот

def main():
    mybot = Updater(settings.API_KEY) # создание экземпляра Updater и передача ему токена бота, который выдал BotFather
    
    logging.info('Bot is starting...')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling() # запуск мониторинга событий создания новых сообщений
    mybot.idle() # команда боту работать вплоть до принудительной остановки


# вызов функции
main()