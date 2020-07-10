import math
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
from util import *



## market price for calls
callPrice = 5

## number of calls bought
nCalls = 100

## strike price of call
strikePrice = 100

## stock price at the time of purchase
stockPriceInit = 100

## time to expiry in days
time = 50 


## volatility (annual in %)
volatilityPercentage = 37.62

volatity = stockPriceInit * volatilityPercentage / 100

## delta
## functionality to compute delta given the other parameters needs to be added
delta = 50

## stocks one would need to buy/sell to get a delta neutral position
nStocks = - nCalls * delta / 100

## theoretical value of the call option
theoreticalValue, _ = MCInt(fTheoreticVal, 100000, stockPriceInit, strikePrice, callPrice, volatity, time)

print(f"Theoretical value of the option is: {theoreticalValue}")



stockPriceFinal = 120

print(f"Net PL if stock price at expiry = {stockPriceFinal}:")

print(f"For underpriced call:")
print(fTotalPL(nCalls, 0, stockPriceFinal, stockPriceInit, strikePrice, callPrice))


print("For accurately priced call:")
print(fTotalPL(nCalls, 0, stockPriceFinal, stockPriceInit, strikePrice, theoreticalValue))


print(f"For underpriced call made delta neutral:")
print(fTotalPL(nCalls, nStocks, stockPriceFinal, stockPriceInit, strikePrice, callPrice))


print(f"For accurately priced call made delta neutral:")
print(fTotalPL(nCalls, nStocks, stockPriceFinal, stockPriceInit, strikePrice, theoreticalValue))


# print(fTotalPL(nCalls, 0, stockPriceFinal, stockPriceInit, strikePrice, callPrice))

# print(fTotalPL(nCalls, 0, stockPriceFinal, stockPriceInit, strikePrice, theoreticalValue))

# print(fTotalPL(nCalls, nStocks, stockPriceFinal, stockPriceInit, strikePrice, callPrice))

# print(fTotalPL(nCalls, nStocks, stockPriceFinal, stockPriceInit, strikePrice, theoreticalValue))
print()

print(f"Expected PL and the variance in PL for different hedging strategies:")

print(f"For underpriced call:")
print(ExpectedPL(fTotalPL, 100000, nCalls, 0, stockPriceInit, strikePrice, callPrice, volatity, time))

print("For accurately priced call:")
print(ExpectedPL(fTotalPL, 100000, nCalls, 0, stockPriceInit, strikePrice, theoreticalValue, volatity, time))

print(f"For underpriced call made delta neutral:")
print(ExpectedPL(fTotalPL, 100000, nCalls, nStocks, stockPriceInit, strikePrice, callPrice, volatity, time))

print("For accurately priced call made delta neutral:")

print(ExpectedPL(fTotalPL, 100000, nCalls, nStocks, stockPriceInit, strikePrice, theoreticalValue, volatity, time))


best = math.inf
best_i = 0

for i in range(100):
	pl, var = ExpectedPL(fTotalPL, 10000, nCalls, -i, stockPriceInit, strikePrice, callPrice, volatity, time)


	if var < best:
		best = var
		best_i = -i

print(f"The position in stock (when one is long {nCalls} calls) that leads to the lowest variance in PL is {best_i}")


