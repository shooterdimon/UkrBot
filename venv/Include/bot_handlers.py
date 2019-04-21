from bot_object import bot

@bot.message_handler(commands=["start"])
def send_welcome(message):
    try:
        bot.send_message(message.chat.id, " Привіт {} {}".format(message.from_user.first_name,message.from_user.last_name))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    bot.polling(none_stop=True)