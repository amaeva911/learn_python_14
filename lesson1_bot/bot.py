from telegram.ext import Updater, CommandHandler


#PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}} #, request_kwargs=PROXY

def greet_user(bot, update):
    print('Аня, привет!')

def main():
    mybot = Updater('635273207:AAG5IfoCXpq308G6ruXmXIqyUUstH7KT5Y8',use_context = True) # создание экземпляра Updater и передача ему токена бота, который выдал BotFather
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)
    
    mybot.start_polling() # запуск мониторинга событий создания новых сообщений
    mybot.idle() # команда боту работать вплоть до принудительной остановки



# вызов функции
main()