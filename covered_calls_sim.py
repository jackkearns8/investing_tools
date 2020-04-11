#!/bin/python3
import numpy as np
import math
import random
import sys
import utils


strikePrice = int(sys.argv[4]) #strike price
	
numAssigned = 0 #number of times the underlying stock is assigned/called away
unrealizedGainsTotal = 0 #total amount of unrealized gains vs holding the underlying
	

def runSimulations():
	# run a 1000 trial monte carlo simulation of underlying stock price movements over the specified number of minutes.
	for i in range(1, 1000):
		currentPrice = utils.initialPrice
		strikePriceHit = False
		for minute in range(0, utils.numMinutes):
			currentPrice = utils.generateNextPrice(currentPrice)
  			
  			if not strikePriceHit and currentPrice > strikePrice:
  				global numAssigned
  				numAssigned += 1
				strikePriceHit = True
  				
  			if strikePriceHit and currentPrice > strikePrice:
  				#guess when the underlying stock will be assigned using a random number generator
  				if random.randint(0, utils.numMinutes - minute) == 1:
  					unrealizedGains = currentPrice - strikePrice
  					global unrealizedGainsTotal
  					unrealizedGainsTotal = unrealizedGainsTotal + unrealizedGains
  					break
  			

def printResults(): 
	print "Total number of times our underlying holdings are assigned out of 1000 trials: "
  	print numAssigned
  	
  	print "Total estimated sacraficed gains: "
  	print unrealizedGainsTotal
	
	
runSimulations()

printResults()