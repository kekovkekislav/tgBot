import telebot
from config import keys,TOKEN
from extensions import Convertion, ConvertionException


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Для начала работы отправьте боту сообщение в виде:\n" \
           "<название валюты которую хотите перевести>,<название валюты в которую перевести>,<количество>.\n" \
           "Пример ввода: рубли,доллар,5000\n" \
           "Увидеть список поддерживаемых валют: /values"

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Список валют: "
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)



@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        user_text = message.text.split(',')

        if len(user_text) != 3:
            raise ConvertionException('Введены лишние параметры.')

        quote, base, amount = user_text
        result = Convertion.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message,f'Ошибка ввода.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать запрос\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {result} '
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
#adasdsda