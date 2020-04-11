#!/bin/python3
import sys
	
	
closerStrikePrice = int(sys.argv[4]) #closer put strike price
fartherStrikePrice = int(sys.argv[5]) #farther put strike price
closerStrikePremium = float(sys.argv[6]) #closer put strike option premium
fartherStrikePremium = float(sys.argv[7]) #farther put strike option premium
	
numCloserHit = 0 #number of times the closer bound put is hit
numFartherHit = 0 #number of times the farther bound put is hit
numBreakEvenHit = 0 #number of times the break even price is hit
	
premiumDiff = closerStrikePremium - fartherStrikePremium
breakEven = closerStrikePrice + premiumDiff #break even price
	
	
def printResults():
	print "Max profit: "
  	print premiumDiff * 100
  	
  	print "Break even: "
  	print breakEven
  	
  	print "Max loss: "
  	print (fartherStrikePrice - closerStrikePrice - premiumDiff) * 100
  			
  	print "Total number of times the underlying breaches the closer bracket out of 1000 trials: "
  	print numCloserHit
  	
  	print "Total number of times the underlying breaches the farther bracket out of 1000 trials: "
  	print numFartherHit
  	
  	print "Total number of times the underlying breaches the break even price out of 1000 trials: "
  	print numBreakEvenHit