# investing_tools 

This is a series of python scripts I use when trading options to assess risk and chances of going in-the-money.

As of now, there are three scripts here.  One for modeling covered calls, and two for vertical spreads.

The aim of the covered call simulator is to model potential gains of writing covered calls vs a simple buy and hold strategy.  The verticals simulators model max profits and losses and the probabilities of wins and losses.

## Usage

python covered_calls_sim.py [time to expiry in minutes] [implied volatility] [current underlying stock price] [strike price]

python vertical_put_spread_sim.py [time to expiry in minutes] [implied volatility] [current underlying stock price] [nearer ITM option price] [farther OTM option price] [nearer price premium] [further price premium]

python vertical_call_spread_sim.py [time to expiry in minutes] [implied volatility] [current underlying stock price] [nearer ITM option price] [farther OTM option price] [nearer price premium] [further price premium]

Note: For SPX, implied volatility is the current VIX price

## Known bugs and issues

1.) Most obvious bug is, these scripts assume trading hours are open 24/7.  I.e., a written option can be called after hours or on weekends.

2.) These scripts assume stock prices movements are 100% random, fitting within a perfect lognormal distribution.  In reality, the lognormal model tends to underestimate more extreme price movements; the 'tails' of the distribution are thicker.
