import os
import requests  # Install requests module first.
import telebot
from keep_alive import keep_alive
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

my_secret = os.environ['TELE_API_KEY']
coinmarketcap_secret = os.environ['X-CMC_PRO_API_KEY']
bot = telebot.TeleBot(my_secret, parse_mode=None)

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': coinmarketcap_secret,
}

session = Session()
session.headers.update(headers)

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

@bot.message_handler(commands=['kucoinokex'])
def KuCoinOKex(message):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=VRA,EFI,IMX,BLOK,NTVRK,KDA'
    response = session.get(url)
    data = json.loads(response.text)
    qtyOfVRA = 821.6159
    qtyOfEFI = 30.7740
    qtyOfIMX = 2.0358
    qtyOfBLOK = 132.196
    qtyOfNTVRK = 2.0807
    qtyOfKDA = 0.5968
    vraPrice = data['data']['VRA']['quote']['USD']['price']
    efiPrice = data['data']['EFI']['quote']['USD']['price']
    imxPrice = data['data']['IMX']['quote']['USD']['price']
    blokPrice = data['data']['BLOK']['quote']['USD']['price']
    ntvrkPrice = data['data']['NTVRK']['quote']['USD']['price']
    kdaPrice = data['data']['KDA']['quote']['USD']['price']

    priceOfVRA = qtyOfVRA * float(vraPrice)
    priceOfEFI = qtyOfEFI * float(efiPrice)
    priceOfIMX = qtyOfIMX * float(imxPrice)
    priceOfBLOK = qtyOfBLOK * float(blokPrice)
    priceOfNTVRK = qtyOfNTVRK * float(ntvrkPrice)
    priceOfKDA = qtyOfKDA * float(kdaPrice)
    current_portfolio_val_in_usdt = priceOfVRA + priceOfEFI + priceOfIMX + priceOfBLOK + priceOfNTVRK + priceOfKDA
    current_portfolio_val_in_INR = current_portfolio_val_in_usdt * float(USDTPriceInINRFromWazirx())
    
    current_portfolio_val_in_usdt = "{:.2f}".format(current_portfolio_val_in_usdt)
    current_portfolio_val_in_INR = "{:.2f}".format(current_portfolio_val_in_INR)
    
    priceStr = "Your Portfolio value in USDT is \n***** " + str(
        current_portfolio_val_in_usdt
    ) + " USDT *****" + "\nYour Portfolio value in INR is \n***** " + u"\u20B9 " + str(
        current_portfolio_val_in_INR)+ " *****" 
    bot.reply_to(message, priceStr)

@bot.message_handler(commands=['twt'])
def TrustWallet(message):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=CELL,DERC,PKR,PARA'
    response = session.get(url)
    data = json.loads(response.text)
    qtyOfCELL = 7.822168
    qtyOfDERC = 1.308382
    qtyOfPKR = 17.00863
    qtyOfPARA = 99.186567
    cellPrice = data['data']['CELL']['quote']['USD']['price']
    dercPrice = data['data']['DERC']['quote']['USD']['price']
    pkrPrice = data['data']['PKR']['quote']['USD']['price']
    paraPrice = data['data']['PARA']['quote']['USD']['price']

    priceOfCELL = qtyOfCELL * float(cellPrice)
    priceOfDERC = qtyOfDERC * float(dercPrice)
    priceOfPKR = qtyOfPKR * float(pkrPrice)
    priceOfPARA = qtyOfPARA * float(paraPrice)
    current_portfolio_val_in_usdt = priceOfCELL + priceOfDERC + priceOfPKR + priceOfPARA
    current_portfolio_val_in_INR = current_portfolio_val_in_usdt * float(USDTPriceInINRFromWazirx())
    
    current_portfolio_val_in_usdt = "{:.2f}".format(current_portfolio_val_in_usdt)
    current_portfolio_val_in_INR = "{:.2f}".format(current_portfolio_val_in_INR)
    
    priceStr = "Your Portfolio value in USDT is \n***** " + str(
        current_portfolio_val_in_usdt
    ) + " USDT *****" + "\nYour Portfolio value in INR is \n***** " + u"\u20B9 " + str(
        current_portfolio_val_in_INR)+ " *****" 
    bot.reply_to(message, priceStr)

@bot.message_handler(commands=['cro'])
def CROPortfolio(message):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=CRO'
    response = session.get(url)
    data = json.loads(response.text)

    qtyOfCRO = 654.88191429
    croPrice = data['data']['CRO']['quote']['USD']['price']
    priceOfCRO = qtyOfCRO * float(croPrice)
    current_portfolio_val_in_usdt = priceOfCRO
    current_portfolio_val_in_INR = current_portfolio_val_in_usdt * float(USDTPriceInINRFromWazirx())
    
    current_portfolio_val_in_usdt = "{:.2f}".format(current_portfolio_val_in_usdt)
    current_portfolio_val_in_INR = "{:.2f}".format(current_portfolio_val_in_INR)
    
    priceStr = "CRO holdings price in USDT is \n***** " + str(
        current_portfolio_val_in_usdt
    ) + " USDT *****" + "\n CRO holdings price in INR is \n***** " + u"\u20B9 " + str(
        current_portfolio_val_in_INR)+ " *****" 
    bot.reply_to(message, priceStr)

@bot.message_handler(commands=['search'])
def search(message):
    searchTxt = "Enter a currency symbol to search..."
    bot.reply_to(message, searchTxt)


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['remaining'])
def remaining(message):
    balanceInUSDT = 31.89
    balanceInINR = balanceInUSDT * float(USDTPriceInINRFromWazirx())
    totalPortfolioInINR = balanceInINR + portfolioInINR()
    balanceInINR = "{:.2f}".format(balanceInINR)
    totalPortfolioInINR = "{:.2f}".format(totalPortfolioInINR)
    priceStr = "Your Remaining balance in USDT is \n***** " + str(balanceInUSDT) + " USDT *****" + "\nYour Remaining balance in INR is \n***** " + u"\u20B9 " + str(
        balanceInINR)+ " *****"
    bot.send_message(message.chat.id, priceStr)

@bot.message_handler(commands=['total'])
def total(message):
    balanceInUSDT = 31.89
    balanceInINR = balanceInUSDT * float(USDTPriceInINRFromWazirx())
    totalPortfolioInINR = balanceInINR + float(portfolioInINR())
    totalPortfolioInINR = "{:.2f}".format(totalPortfolioInINR)
    priceStr = "Total Portfolio In INR is \n***** " + u"\u20B9 " + str( totalPortfolioInINR ) + " *****"
    bot.send_message(message.chat.id, priceStr)

@bot.message_handler(commands=['binance'])
def BinancePortfolio(message):
    qtyOfDot = 2.238005
    qtyOfAda = 10.03249
    qtyOfSol = 0.258681
    qtyOfMatic = 7.6923
    qtyOfLuna = 0.47
    qtyOfLink = 0.508491
    qtyOfTheta = 2.018979
    qtyOfFTM = 6
    qtyOfSKL = 32
    qtyOfCake = 0.64
    qtyOfXEC = 53570.38
    qtyOfSHIB = 195926
    qtyOfWRX = 6.7
    
    priceOfDot = qtyOfDot * float(getPriceOfaCoinInUSDT("DOT"))
    priceOfAda = qtyOfAda * float(getPriceOfaCoinInUSDT("ADA"))
    priceOfSol = qtyOfSol * float(getPriceOfaCoinInUSDT("SOL"))
    priceOfMatic = qtyOfMatic * float(getPriceOfaCoinInUSDT("MATIC"))
    priceOfLuna = qtyOfLuna * float(getPriceOfaCoinInUSDT("LUNA"))
    priceOfLink = qtyOfLink * float(getPriceOfaCoinInUSDT("LINK"))
    priceOfTheta = qtyOfTheta * float(getPriceOfaCoinInUSDT("THETA"))
    priceOfFTM = qtyOfFTM * float(getPriceOfaCoinInUSDT("FTM"))
    priceOfSKL = qtyOfSKL * float(getPriceOfaCoinInUSDT("SKL"))
    priceOfCake = qtyOfCake * float(getPriceOfaCoinInUSDT("CAKE"))
    priceOfXEC = qtyOfXEC * float(getPriceOfaCoinInUSDT("XEC"))
    priceOfSHIB = qtyOfSHIB * float(getPriceOfaCoinInUSDT("SHIB"))
    priceOfWRX = qtyOfWRX * float(getPriceOfaCoinInUSDT("WRX"))
    current_portfolio_val_in_usdt = priceOfDot + priceOfAda + priceOfSol + \
        priceOfMatic + priceOfLuna + priceOfLink + priceOfTheta + priceOfFTM \
        + priceOfSKL + priceOfCake + priceOfXEC + priceOfSHIB + priceOfWRX
    current_portfolio_val_in_INR = current_portfolio_val_in_usdt * float(USDTPriceInINRFromWazirx())
    
    current_portfolio_val_in_usdt = "{:.2f}".format(current_portfolio_val_in_usdt)
    current_portfolio_val_in_INR = "{:.2f}".format(current_portfolio_val_in_INR)
    
    priceStr = "Your Portfolio value in USDT is \n***** " + str(
        current_portfolio_val_in_usdt
    ) + " USDT *****" + "\nYour Portfolio value in INR is \n***** " + u"\u20B9 " + str(
        current_portfolio_val_in_INR)+ " *****" 
    bot.send_message(message.chat.id, priceStr)

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

    if (message.text).upper() == "USDT":
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

def getPriceOfaCoinInUSDT(coin):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=" + coin + 'USDT'
    response = requests.get(url)
    data = response.json()
    priceInUSDT = float(data['price'])
    # priceInUSDT = "{:.2f}".format(priceInUSDT)
    return priceInUSDT

def USDTPriceInINRFromWazirx():
    url = "https://api.wazirx.com/api/v2/trades?market=usdtinr"
    response = requests.get(url)
    data = response.json()
    return data[0]['price']

def portfolioInINR():
    qtyOfDot = 0.67
    qtyOfAda = 8.63
    qtyOfSol = 0.37
    priceOfDot = qtyOfDot * float(getPriceOfaCoinInUSDT("DOT"))
    priceOfAda = qtyOfAda * float(getPriceOfaCoinInUSDT("ADA"))
    priceOfSol = qtyOfSol * float(getPriceOfaCoinInUSDT("SOL"))
    current_portfolio_val_in_usdt = priceOfDot + priceOfAda + priceOfSol
    current_portfolio_val_in_INR = current_portfolio_val_in_usdt * float(USDTPriceInINRFromWazirx())
    return current_portfolio_val_in_INR

bot.polling(none_stop=False, interval=0, timeout=20)

#binance
#kucoinokex
#twt
#cro