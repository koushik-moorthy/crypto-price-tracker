import os
import requests  # Install requests module first.
import telebot
from keep_alive import keep_alive

my_secret = os.environ['TELE_API_KEY']
bot = telebot.TeleBot(my_secret, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,  
        "Welcome to CryptoCurrency Price Tracker! Enter the currency you want to search..."
    )


@bot.message_handler(commands=['greet'])
def greet(message):
    greetMsg = "Hey! " + message.chat.first_name + " Hows it going?"
    bot.reply_to(message, greetMsg)


@bot.message_handler(commands=['search'])
def search(message):
    searchTxt = "Enter a currency symbol to search..."
    bot.reply_to(message, searchTxt)


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")


def validate_request(message):
    request = message.text.split()
    if len(request) != 1:
        bot.send_message(message.chat.id,
                         "Sorry, I can't process your request at the moment!")
        return False
    else:
        return True


@bot.message_handler(func=validate_request)
def echo_all(message):

    if message.text == "USDT" or message.text == "usdt":
        priceInINR = USDTPriceInINRFromWazirx()
        priceInINR = "Price of 1 USDT in INR is " + u"\u20B9" + priceInINR
        bot.send_message(message.chat.id, priceInINR)
    else:
        try:
            theMessage = (message.text).upper()
            price = getPriceOfaCoin(theMessage)
            bot.send_message(message.chat.id, price)
        except Exception as e:
            bot.send_message(message.chat.id, "Invalid Currency")
            print("Invalid Currency ", e)


keep_alive()


def getPriceOfaCoin(coin):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=" + coin + 'USDT'
    response = requests.get(url)
    data = response.json()
    priceInUSDT = float(data['price'])
    priceInINR = float(USDTPriceInINRFromWazirx()) * float(priceInUSDT)
    priceInUSDT = "{:.2f}".format(priceInUSDT)
    priceInINR = "{:.2f}".format(priceInINR)
    priceStr = "Price of " + coin + " in USDT is " + str(
        priceInUSDT
    ) + "USDT" + "\nPrice of " + coin + " in INR is " + u"\u20B9" + str(
        priceInINR)
    return priceStr


def USDTPriceInINRFromWazirx():
    url = "https://api.wazirx.com/api/v2/trades?market=usdtinr"
    response = requests.get(url)
    data = response.json()
    return data[0]['price']


bot.polling(none_stop=False, interval=0, timeout=20)
