#!/bin/python3
import mibian
import sys

underlyingPrice = float(sys.argv[1]) 
strikePrice = float(sys.argv[2]) 
interestRate = float(sys.argv[3]) 
daysToExpiration = float(sys.argv[4]) 
optionPrice = float(sys.argv[5]) 
isCall = sys.argv[6].lower() == 'true'
	
if isCall: 
	c = mibian.BS([underlyingPrice, strikePrice, interestRate, daysToExpiration], callPrice=optionPrice)
	print c.impliedVolatility
else:
	c = mibian.BS([underlyingPrice, strikePrice, interestRate, daysToExpiration], putPrice=optionPrice)
	print c.impliedVolatility