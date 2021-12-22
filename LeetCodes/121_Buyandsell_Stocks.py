prices = [7,1,5,3,6,4]

def maxprofit ():
    if len(prices) <= 1:
        return 0

    max_profit = 0
    min_buy = float('inf')
    for price in prices:
        min_buy = min(min_buy, price)
        max_profit = max(max_profit, price - min_buy)
    return max_profit

if __name__ == "__main__":
    print(maxprofit())