
def coin_change_brute(n):
    buffer = [n+1]*(n+1)
    buffer[0] = 0

    for amount in range(1, n+1):
        for coin in coins:
            if amount - coin >= 0:
                buffer[amount] = min(buffer[amount], 1+buffer[amount-coin])

    return buffer[amount] if buffer[amount] != amount+1 else -1


if __name__ == '__main__':
    n = 11
    coins = [1, 2, 5]
    print(f"fewest number of coins needed to make {n} is {coin_change_brute(n)}")