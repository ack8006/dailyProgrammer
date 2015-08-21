#http://api.bitcoincharts.com/v1/trades.csv?

#take exchange, currency
#Your API should return the current value of Bitcoin according to that exchange in that currency.

#symbol,currency,bid, ask,latest_trade,n_trades,high,low,close,previous_close,volume,currency_volume

#ToDo:
#sqlLite for symbols that don't work
#302 if no data

#http://api.bitcoincharts.com/v1/trades.csv?symbol=bitfinexUSD

import requests

class BitcoinPricer(object):

	def getPrice(self, exchange, symbol):
		bitcoinURL = "http://api.bitcoincharts.com/v1/trades.csv?"
		response = requests.get(bitcoinURL, params={'symbol': exchange+symbol})
		if response.ok:
			page = response.text
			self.printPrice(page)
		else:
			print "you done fucked up"

	def printPrice(self, page):
		lines = page.splitlines()
		print lines[0].split(',')[1]

def main():
	exchange = raw_input('Please Select Exchange -> ')
	fx = raw_input('Please Select FX -> ')
	#exchange = 'bitfinex'
	#fx = 'USD'

	bp = BitcoinPricer()
	price = bp.getPrice(exchange, fx)

if __name__ == "__main__":
	main()
