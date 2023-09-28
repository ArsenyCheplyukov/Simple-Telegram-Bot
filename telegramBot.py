import config
import telebot
import random

bot = telebot.TeleBot(config.TOKEN)

tasks = []

@bot.message_handler(commands=["rules"])
def rules_handler(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, 'Задания нельзя смотреть')
    bot.send_message(message.chat.id, 'Задания обязательно выполняются в день прокрутки')
    bot.send_message(message.chat.id, 'Сложные задания помечаются звёздочкой и выполняются по мере возможности выполнения')

@bot.message_handler(commands=["start"])
def start_handler(message): # Название функции не играет никакой роли
    tasks.clear()

@bot.message_handler(commands=["stop"])
def start_handler(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, random.choice(tasks))

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    tasks.append(message.text)

if __name__ == '__main__':
    bot.remove_webhook()
    bot.infinity_polling()