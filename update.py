'''
Run this at least once a week to update minimum quantitiy and minimum price
'''

from binance.client import Client
import sys

api_key = "x"
api_secret = "x"

client = Client(api_key, api_secret)

fileData = open('coinlist.txt', 'r')
lines=fileData.readlines()

print("Starting...")
isFinished = 0
myfile = open('Coins/precision.txt', 'w')
for line in lines:
	print("in loop")

	ticker = line.strip("\n") + 'BTC'
	info = client.get_symbol_info(ticker)
	
	#gets the necessary information via api and stores into a dictionary
	sInfo = line.strip("\n") + '/' + info['filters'][1]['minQty'] + '/' + info['filters'][0]['minPrice']
	myfile.write("%s\n" % sInfo)
	
print("Finished!")
myfile.close()	