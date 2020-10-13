# investing_tools 

This is a series of python scripts I use when trading options to assess risk and chances of going in-the-money.

As of now, there are five scripts here.  One for modeling covered calls, two for vertical spreads, and two for calculating IV and historic standard dev over a # of days.

The aim of the covered call simulator is to model potential gains of writing covered calls vs a simple buy and hold strategy.  The verticals simulators model max profits and losses and the probabilities of wins and losses.


## Usage

python covered_calls_sim.py [days to expiry] [implied vol] [underlying price] [strike price]

python vertical_put_spread_sim.py [days to expiry] [implied vol] [underlying price] [nearer ITM option price] [farther OTM option price] [nearer price premium] [further price premium]

python vertical_call_spread_sim.py [days to expiry] [implied vol] [underlying price] [nearer ITM option price] [farther OTM option price] [nearer price premium] [further price premium]

python iv_calculator.py [underlying price] [strike price] [interest rate] [days to expiration] [option price] [boolean: is call option?]

python sigma_calculator.py [symbol] [num days back]

## Known bugs and issues

1.) These scripts assume stock prices movements are 100% random, fitting within a perfect lognormal distribution.  In reality, the lognormal model tends to underestimate more extreme price movements; the 'tails' of the distribution are thicker.
