#!/bin/python3
import sys
import yfinance as yf
import math  

ticker = sys.argv[1]
days = sys.argv[2]

stock = yf.Ticker(ticker)

daysStr = days + "d"
hist = stock.history(period=daysStr)

sigma = hist["Close"].std()
annualizedSigma = sigma*math.sqrt(365/float(days))

print(annualizedSigma)