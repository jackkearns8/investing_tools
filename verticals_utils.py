#!/bin/python3
import sys
import utils


def runSimulations(isCallSpread):
	CLOSER_STRIKE_PRICE = float(sys.argv[4]) #closer option strike price
	FARTHER_STRIKE_PRICE = float(sys.argv[5]) #farther option strike price
	CLOSER_STRIKE_PREMIUM = float(sys.argv[6]) #closer option strike option premium
	FARTHER_STRIKE_PREMIUM = float(sys.argv[7]) #farther option strike option premium
	
	numCloserHit = 0 #number of times the closer bound option is hit
	numFartherHit = 0 #number of times the farther bound option is hit
	numBreakEvenHit = 0 #number of times the break even price is hit
	
	premiumDiff = CLOSER_STRIKE_PREMIUM - FARTHER_STRIKE_PREMIUM
	breakEven = CLOSER_STRIKE_PRICE + premiumDiff 

	# run a 1000 trial monte carlo simulation of the underlying stock price movements over the specified number of minutes.
	for i in range(1, 1000):
		currentPrice = utils.INITIAL_PRICE
		closerStrikePriceHit = False
		fartherStrikePriceHit = False
		breakEvenHit = False
		for minute in range(0, utils.NUM_MINUTES):
			currentPrice = utils.generateNextPrice(currentPrice)
  			
  			if isCallSpread: 
  				if not closerStrikePriceHit and currentPrice > CLOSER_STRIKE_PRICE:
  					numCloserHit = numCloserHit + 1
  					closerStrikePriceHit = True
  				
  				if not fartherStrikePriceHit and currentPrice > FARTHER_STRIKE_PRICE:
  					numFartherHit = numFartherHit + 1
  					fartherStrikePriceHit = True
  				
  				if not breakEvenHit and currentPrice > breakEven:
  					numBreakEvenHit = numBreakEvenHit + 1
  					breakEvenHit = True
  			
  			#else must be a put spread
  			else:
  				if not closerStrikePriceHit and currentPrice < CLOSER_STRIKE_PRICE:
  					numCloserHit = numCloserHit + 1
  					closerStrikePriceHit = True
  				
  				if not fartherStrikePriceHit and currentPrice < FARTHER_STRIKE_PRICE:
  					numFartherHit = numFartherHit + 1
  					fartherStrikePriceHit = True
  				
  				if not breakEvenHit and currentPrice > breakEven:
  					numBreakEvenHit = numBreakEvenHit + 1
  					breakEvenHit = True
  	
  	maxProfit = premiumDiff * 100
  	maxLoss = (FARTHER_STRIKE_PRICE - CLOSER_STRIKE_PRICE - premiumDiff) * 100
  	printResults(maxProfit, breakEven, maxLoss, numCloserHit, numFartherHit, numBreakEvenHit)
	
	
def printResults(maxProfit, brkEven, maxLoss, nmbrClsrHit, nmbrFthrHit, nmbrBrkEvenHit):
	print "Max profit: "
  	print maxProfit
  	
  	print "Break even: "
  	print brkEven
  	
  	print "Max loss: "
  	print maxLoss
  			
  	print "Total number of times the underlying breaches the closer bracket out of 1000 trials: "
  	print nmbrClsrHit
  	
  	print "Total number of times the underlying breaches the farther bracket out of 1000 trials: "
  	print nmbrFthrHit
  	
  	print "Total number of times the underlying breaches the break even price out of 1000 trials: "
  	print nmbrBrkEvenHit