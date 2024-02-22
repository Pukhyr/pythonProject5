import datetime


import telebot

from config import TOKEN
from db import get_notes_from_db, createdb

bot = telebot.TeleBot(TOKEN)

def get_welcome() -> str:
    current_time = datetime.datetime.now()
    if 0<= current_time.hour <6:
        return 'Доброй ночи!'
    if 6<= current_time.hour <12:
        return 'Доброе утро!'
    if 12<= current_time.hour <18:
        return 'Добрый день!'
    else:
        return 'Добрый вечер!'

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = f'{get_welcome()} Я бот для твоих заметок)\n\n'\
           f'Список команд:\n'\
           f'/get_all - получить все имеющиеся заметки\n'\
           f'/add_note - добавить заметку \n'\
           f'/delete_note - удалить заметку'

    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['get_all'])
def get_all(message: telebot.types.Message):
    notes = get_notes_from_db()




if __name__=='__main__':
    createdb()
    print ('Бот запущен')
    bot.infinity_polling()



