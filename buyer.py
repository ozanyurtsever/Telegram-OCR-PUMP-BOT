from binance.client import Client
from binance.enums import *
import sys
import time
from decimal import Decimal
from pathlib import Path


from PIL import Image
import pytesseract
import string

#Choose your tesseract-ocr folder
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

api_key = "x"
api_secret = "x"

#list of the name of the cryptocurrencies on binance
fileData = open('Coins/coinlist.txt', 'r')
lines=fileData.readlines()

client = Client(api_key, api_secret)
amountToTrade = 0.20

def buy_currency(currency):
	ticker = currency + 'BTC'
	print(ticker)
	quantity = int(amountToTrade / float(client.get_orderbook_ticker(symbol=ticker)['askPrice']))
	order = client.create_order(
		symbol=ticker,
		side=Client.SIDE_BUY,
		type=Client.ORDER_TYPE_MARKET,
		quantity=quantity)
	print("-----------ALIS------------")
	print(order) 
	
def round_down(num,digits):
	factor = 10.0 ** digits
	return int(num * factor) / factor



def sell_currency(currency):
    
	ticker = currency + 'BTC'
	
	
	info = client.get_symbol_info(ticker)

	fiyat = float(client.get_recent_trades(symbol=ticker)[0]['price'])
	fiyat = fiyat + fiyat * 0.50
	minQty = str(float(info['filters'][1]['minQty']))
	numbers = sum(c.isdigit() for c in minQty)   # counts how many digit in minqty to adjust precision
	minPrc = info['filters'][0]['minPrice']
	
	#counts the number of digits in minPrc and adjust precision
	i = 0
	for c in minPrc:
		if c == '0':
			i = i + 1
		elif c == '.':
			continue
		else :
			break
	
	sell_price = "{:0.{}f}".format(fiyat, i) # adjusts the variable 'fiyat' based on precision
	
	# adjusts the quantity
	miktar = float(client.get_asset_balance(asset = currency)['free'])
	if(numbers == 2):
		miktar = int(miktar)
	else:
		miktar = round_down(miktar, numbers - 1)
	

	print("-----------SATIS------------")
	
	
	sat = client.order_limit_sell(symbol = ticker, quantity = miktar, price = sell_price)
	print(sat)

print("Starting...")
isFinished = 0
myfile = open('info.txt', 'w')
for line in lines:
	print("in loop")

	ticker = line.strip("\n") + 'BTC'
	info = client.get_symbol_info(ticker)
	sInfo = line.strip("\n") + '/' + info['filters'][1]['minQty'] + '/' + info['filters'][0]['minPrice']
	myfile.write("%s\n" % sInfo)
	
print("Finished!")
myfile.close()	


hasImage = False
my_file = Path("output.jpg")

while(hasImage == False):

	if my_file.is_file():
		hasImage = True
		

printable = set(string.printable)

while True:

	try:

		imgTXT = filter(lambda x: x in printable, pytesseract.image_to_string(Image.open('output.jpg'), lang='eng'))

	except:

		continue

	break



print(imgTXT)
pattern = ""
for line in lines:
	if line in imgTXT:
		pattern = line
		
		
pattern = pattern.strip("\n")



buy_currency(pattern)
sell_currency(pattern)