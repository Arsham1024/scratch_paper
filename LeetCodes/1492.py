# Speed: faster than 15.37%
# Space: Less than 48%
def version1(n , k):
    factors = [1]
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
    # Every number is their own factor
    factors.append(n)

    print(factors)
    return factors[k-1] if len(factors) >= k else -1

if __name__ == "__main__":
    n = 7
    k = 2
    print(version1(n , k))