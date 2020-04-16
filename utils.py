#!/bin/python3
import numpy as np
import math
import sys
	
	
MINUTES_IN_YEAR = 60*24*365
NUM_MINUTES = int(sys.argv[1]) #num minutes to option expiration
IV = float(sys.argv[2]) #implied volatility of the underlying
INITIAL_PRICE = float(sys.argv[3]) #current underlying price
	

def generateNextPrice(currentPrice): 
	#convert implied volatility to a normal standard deviation
	sigma = INITIAL_PRICE*IV/(100*MINUTES_IN_YEAR**0.5)
			
	# stock price movements roughly follow a lognormal distribution, so we must normalize our mean and st dev
	normalStd = math.sqrt(math.log(1 + (sigma/currentPrice)**2))
	normalMean = math.log(currentPrice) - normalStd**2 / 2
			
  	nextPrice = np.random.lognormal(normalMean, normalStd)
  		
  	return nextPrice