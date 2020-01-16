import time
import json
import requests

lastTradingMode = "undefined"
lastPrice = "2.40"

# Price from API
currentPrice = "2.70"

# Set mode in file
def setTradingMode(mode):
	with open('tradingMode.txt', 'r+') as f:
		f.write(mode)
		f.truncate()
		
# Get last trade action from file
def getTradingMode():
	with open('tradingMode.txt', 'r+') as f:
		global lastTradingMode 
		lastTradingMode = "".join(f.readlines()[0:])


# Set last price sold/bought for
def setLastPrice(price):
	with open('lastPrice.txt', 'r+') as f:
		f.write(str(price))
		f.truncate()

# Get last trade action from file
def getLastPrice():
	with open('lastPrice.txt', 'r+') as f:
		global lastTradingMode 
		lastPrice = "".join(f.readlines()[0:])

# Perform trade
def getSellOrBuyAmount(action, amount):
	if (action == "sell"):
		return float(lastPrice) + 0.30
	elif (action == "buy"):
		return float(lastPrice) - 0.30

def checkWhetherToTradeOrNot():
	print("I'm going to check if you should trade...")
	time.sleep(3)
	if (lastTradingMode == "sell"):
		print("your last trade was to sell, so now we need to check if you should buy lower")
		#time.sleep(3)

		if (getSellOrBuyAmount("buy", lastPrice) != currentPrice):
			print("According to your logic, you should not buy right now, it's still too high")
			wantedPrice = getSellOrBuyAmount('buy', lastPrice)
			print ("you want to buy when it is: %(wp)s}" % {'wp': wantedPrice})
			
		elif(getSellOrBuyAmount("buy", lastPrice) >= currentPrice):
			print("Same or higher: buy buy buy")
		else:
			print("ELSE")

		print("After if statement")

	elif (lastTradingMode == "buy"):
		print("your last trade was to buy, so now we need to check if you should sell higher")
		time.sleep(3)


# App Start - Should be very last define App. 
def appStart():

	# Check Binance API Connection 

	apiURL = "https://api.binance.com/api/v3/account"

	params = dict(
	    origin='Chicago,IL',
	    destination='Los+Angeles,CA',
	    waypoints='Joplin,MO|Oklahoma+City,OK',
	    sensor='false'
	)

	resp = requests.get(url=apiURL, params=params)
	data = resp.json()

	print(data	)


	# getTradingMode()
	# setLastPrice(2.70)

	# checkWhetherToTradeOrNot()
	

	# if (lastTradingMode == "buy"):
	# 		print("This means I should sell")
	# 		setTradingMode("sell")
	# 		setLastPrice(3.0)
	# 		print("The last price was " + lastPrice)

	# 		getSellOrBuyAmount("buy", 3.0)

	# elif (lastTradingMode == "sell"):
	# 		print("I should buy")
	# 		setTradingMode("buy")
	# 		setLastPrice(2.70)

#setTradingMode("sell");

#Run App
appStart();


