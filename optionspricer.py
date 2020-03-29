#!/bin/python3
import numpy as np
import math
import random
	
	
def runSimulations():
	MinutesInYear = 60*24*365
	NumMinutes = 60*8*7
	Vix = 66
	InitialPrice = 100
	StrikePrice = 104
	
	numCallsAway = 0
	unrealizedGainsTotal = 0

	for i in range(1, 1000):
		currentPrice = InitialPrice
		strikePriceHit = False
		for minute in range(0, NumMinutes):
			sigma = InitialPrice*Vix/(100*MinutesInYear**0.5)
			#stock price changes roughly follow a lognormal distribution
			normal_std = math.sqrt(math.log(1 + (sigma/currentPrice)**2))
			normal_mean = math.log(currentPrice) - normal_std**2 / 2
			#print currentPrice
  			currentPrice = np.random.lognormal(normal_mean, normal_std)
  			if not strikePriceHit and currentPrice > StrikePrice:
  				numCallsAway = numCallsAway + 1
  				strikePriceHit = True
  				
  			if strikePriceHit and currentPrice > StrikePrice:
  				if random.randint(0, NumMinutes - minute) == 1:
  					unrealizedGains = currentPrice - StrikePrice
  					unrealizedGainsTotal = unrealizedGainsTotal + unrealizedGains
  					break
  			
  			
  			#if strikePriceHit:
  				#document.getElementById("callsInfoHolder").innerHTML = document.getElementById("callsInfoHolder").innerHTML + "<br>" + currentPrice;
  			
  	print "Total number of times called away out of 1000: "
  	print numCallsAway
  	print "Total estimated sacraficed gains: "
  	print unrealizedGainsTotal
	
runSimulations()