import scipy
import numpy as np

class BlackScholes:
    """
    Black Scholes Model implemented in an object oriented approach

    Important Assumptions:
    - Options exercised at expiration
    - Volatility remains constant
    - No transaction costs
    - Fractional shares are allowed
    - Stock pays no dividend
    - Stock follows a random walk and volatility follows a log-normal distribution
    """
    
    def __init__(self, S, X, t, r, sgma):
        self.S = S # underlying stock price
        self.X = X # exercise price
        self.t = t # time to expiration in years
        self.r = r # interest rate
        self.sgma = sgma # volatility in percent

    def N(self, x):
        return scipy.stats.norm.cdf(x)
    
    def d1(self):
        return (np.log(self.S / self.X) + (self.r + (np.square(self.sgma)/2)) * self.t) / (self.sgma * np.sqrt(self.t))

    def d2(self):
        return self.d1() - (self.sgma * np.sqrt(self.t))
    
    def call(self):
        return self.S * self.N(self.d1()) - self.N(self.d2()) * self.X * np.exp(-1 * self.r * self.t)
    
    def put(self):
        return -self.S * self.N(-self.d1()) + self.N(-self.d2()) * self.X * np.exp(-self.r * self.t)