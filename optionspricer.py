#!/bin/python3
import numpy as np
import math
import random
import sys
	
	
def runSimulations():
	MINUTES_IN_YEAR = 60*24*365
	numMinutes = int(sys.argv[1]) #num minutes to option expiration
	vix = int(sys.argv[2]) #volatility index
	initialPrice = int(sys.argv[3]) #current SPX price
	strikePrice = int(sys.argv[4]) #strike price
	
	numAssgined = 0 #number of times the underlying stock is called away
	unrealizedGainsTotal = 0 #total amount of unrealized gains vs holding SPX

	# run a 1000 trial monte carlo simulation of SPX stock price movements over the specified number of minutes.
	for i in range(1, 1000):
		currentPrice = initialPrice
		strikePriceHit = False
		for minute in range(0, numMinutes):
			sigma = initialPrice*vix/(100*MINUTES_IN_YEAR**0.5)
			
			# stock price movements roughly follow a lognormal distribution, so we must normalize our mean and st dev
			normalStd = math.sqrt(math.log(1 + (sigma/currentPrice)**2))
			normalMean = math.log(currentPrice) - normalStd**2 / 2
			
  			currentPrice = np.random.lognormal(normalMean, normalStd)
  			
  			if not strikePriceHit and currentPrice > strikePrice:
  				numAssgined = numAssgined + 1
  				strikePriceHit = True
  				
  			if strikePriceHit and currentPrice > strikePrice:
  				#guess when the underlying stock will be assigned using a random number generator
  				if random.randint(0, numMinutes - minute) == 1:
  					unrealizedGains = currentPrice - strikePrice
  					unrealizedGainsTotal = unrealizedGainsTotal + unrealizedGains
  					break
  			
  	print "Total number of times our SPX holdings are assigned out of 1000 trials: "
  	print numAssgined
  	
  	print "Total estimated sacraficed gains: "
  	print unrealizedGainsTotal
	
runSimulations()