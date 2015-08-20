#http://api.bitcoincharts.com/v1/trades.csv?

#take exchange, currency
#Your API should return the current value of Bitcoin according to that exchange in that currency.

#symbol,currency,bid, ask,latest_trade,n_trades,high,low,close,previous_close,volume,currency_volume

#ToDo:
#sqlLite for symbols that don't work
#302 if no data

#http://api.bitcoincharts.com/v1/trades.csv?symbol=bitfinexUSD

import csv
import urllib2

class BitcoinPricer(object):

	def __init__(self, exchange, symbol, fileType = 'csv'):
		self.bitcoinURL = "http://api.bitcoincharts.com/v1/trades.{}?symbol={}".format(fileType, exchange+symbol) 
		print self.bitcoinURL

	def getPrice(self):
		response = urllib2.urlopen(self.bitcoinURL)
		pageCSV = csv.reader(response)
		print pageCSV.next()[1]

def main():
	exchange = raw_input('Please Select Exchange -> ')
	fx = raw_input('Please Select FX -> ')
	#exchange = 'bitfinex'
	#fx = 'USD'

	bp = BitcoinPricer(exchange, fx)
	price = bp.getPrice()

if __name__ == "__main__":
	main()
