# Hedging

## Work In Progress

##An implementation of the Black-Scholes Model

The Black-Scholes model is a  mathematical model that models the dynamics of prices of options contracts.
This is a fairly simplified (and slightly adjusted) version which doesn't take interest or dividends into consideration.

Using this code, one can compute the theoretical price of call options given their strike price, time to expiry, the current stock price and its volatility.

One can also compute their P/L given the stock price at the time of expiry for whatever position they hold in call options and stocks.

Finally, one can also compute their expected P/L (over all possible stock prices at the time of expiry) for any such given position.
