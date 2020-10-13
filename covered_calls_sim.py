#!/bin/python3
import random
import utils
import sys
	

def runSimulations():
	strikePrice = float(sys.argv[4])
	numAssigned = 0 #number of times the underlying stock is assigned/called away
	totalOpportunityCost = 0 #total amount of unrealized gains vs holding the underlying

	# run a 1000 trial monte carlo simulation of underlying stock price movements over the specified number of minutes.
	for i in range(1, 1000):
		currentPrice = utils.initialPrice
		strikePriceHit = False
		for minute in range(0, utils.numDays):
			currentPrice = utils.generateNextPrice(currentPrice)
  			
  			if not strikePriceHit and currentPrice > strikePrice:
  				numAssigned += 1
				strikePriceHit = True
  				
  			if strikePriceHit and currentPrice > strikePrice:
  				#guess when the underlying stock will be assigned using a random number generator
  				if random.randint(0, utils.numDays - minute) == 1:
  					unrealizedGains = currentPrice - strikePrice
  					totalOpportunityCost = totalOpportunityCost + unrealizedGains
  					break
  					
  	printResults(numAssigned, totalOpportunityCost)
  			

def printResults(nmbrAssigned, opportunityCost):
	print "Total number of times our underlying holdings are assigned out of 1000 trials: "
  	print nmbrAssigned
  	
  	print "Total opportunity cost vs buy-and-hold: "
  	print opportunityCost
	
	
runSimulations()