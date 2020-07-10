import math
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad

def expiryValue(p, strikePrice):

	return max(p - strikePrice, 0)

def fTheoreticVal(p, stockPriceInit, strikePrice, callPrice):

	return expiryValue(p, strikePrice)

def fCallPL(p, stockPriceInit, strikePrice, callPrice):

	return expiryValue(p, strikePrice) - callPrice

def fStockPL(p, stockPriceInit, strikePrice, callPrice):

	return p - stockPriceInit

def fTotalPL(nCalls, nStocks, p, stockPriceInit, strikePrice, callPrice):

	return nCalls * fCallPL(p, stockPriceInit, strikePrice, callPrice) + nStocks * fStockPL(p, stockPriceInit, strikePrice, callPrice)


def MCInt(f, samples, stockPriceInit, strikePrice, callPrice, volatity, time):

	z = np.zeros(samples)

	for i in range(samples):
		p = np.random.normal(stockPriceInit, volatity / math.sqrt(256/time))
		z[i] = f(p, stockPriceInit, strikePrice, callPrice)

	return np.mean(z), np.std(z)

def ExpectedPL(f, samples, nCalls, nStocks, stockPriceInit, strikePrice, callPrice, volatity, time):

	z = np.zeros(samples)

	for i in range(samples):
		p = np.random.normal(stockPriceInit, volatity / math.sqrt(256/time))
		z[i] = f(nCalls, nStocks, p, stockPriceInit, strikePrice, callPrice)

	return np.mean(z), np.std(z)

