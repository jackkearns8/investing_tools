#!/bin/python3
import utils
import verticals_utils
	
	
def runSimulations():
	# run a 1000 trial monte carlo simulation of the underlying stock price movements over the specified number of minutes.
	for i in range(1, 1000):
		currentPrice = utils.initialPrice
		closerStrikePriceHit = False
		fartherStrikePriceHit = False
		breakEvenHit = False
		for minute in range(0, utils.numMinutes):
			currentPrice = utils.generateNextPrice(currentPrice)
  			
  			if not closerStrikePriceHit and currentPrice > verticals_utils.closerStrikePrice:
  				verticals_utils.numCloserHit = verticals_utils.numCloserHit + 1
  				closerStrikePriceHit = True
  				
  			if not fartherStrikePriceHit and currentPrice > verticals_utils.fartherStrikePrice:
  				verticals_utils.numFartherHit = verticals_utils.numFartherHit + 1
  				fartherStrikePriceHit = True
  				
  			if not breakEvenHit and currentPrice > verticals_utils.breakEven:
  				verticals_utils.numBreakEvenHit = verticals_utils.numBreakEvenHit + 1
  				breakEvenHit = True
	
	
runSimulations()

verticals_utils.printResults()