#!/bin/python3
import numpy as np
import math
import sys
	
	
DAYS_IN_YEAR = 365
numDays = int(sys.argv[1]) #num minutes to option expiration
iv = float(sys.argv[2]) #implied volatility of the underlying
initialPrice = float(sys.argv[3]) #current underlying price
	

def generateNextPrice(currentPrice): 
	#convert implied volatility to a normal standard deviation
	sigma = initialPrice*iv/(100*DAYS_IN_YEAR**0.5)
			
	# stock price movements roughly follow a lognormal distribution, so we must normalize our mean and st dev
	normalStd = math.sqrt(math.log(1 + (sigma/currentPrice)**2))
	normalMean = math.log(currentPrice) - normalStd**2 / 2
			
  	nextPrice = np.random.lognormal(normalMean, normalStd)
  		
  	return nextPrice