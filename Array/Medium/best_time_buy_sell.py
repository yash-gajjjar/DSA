import math

def maxProfit(prices):
    min_price, max_profit = math.inf, 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

maxProfit([7,1,5,3,6,4])