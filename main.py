import telebot
import random

candys = 117
mode = ' '

bot = telebot.TeleBot('5900301929:AAFzHGw1NRHwvF1HCj3m_jdnU8ft4s-ij-U')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    global mode
    play_hod = ['Пользователь', 'Бот']
    mode = random.choice(play_hod)
    if mode == 'Пользователь':
        bot.send_message(m.chat.id, 'Начинайте игру, введите количество конфет от 1 до 28')
    if mode == 'Бот':
        bot.send_message(m.chat.id, 'Бот сделал выбор, введите количество конфет от 1 до 28')
    
@bot.message_handler(content_types=["text"])
def handle_text(message):
    hod = 0
    global candys
    global mode
    if int(message.text) > 29:
        bot.send_message(message.chat.id, 'Введите число от 1 до 28')
    else:
        bot_candys = random.randint(1, 29)
        candys = candys - int(message.text) - int(bot_candys)
        bot.send_message(message.chat.id, 'Ваш выбор: ' + message.text + ' '+ 'Бот взял: '\
        +  ' '+ str(bot_candys) + ' ' + 'Осталось: ' + str(candys))
        if mode == 'Пользователь':
            mode == 'Бот'
        if mode == 'Бот':
            mode == 'Пользователь'
        if candys <29:
            bot.send_message(message.chat.id, 'Победил ' + mode)
 
print('server run')
bot.infinity_polling()

