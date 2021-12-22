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

# Clever version but not intuitive!
# Speed: faster than 5%
# Space: Less than 13.7%
def version2(n , k):
    for i in range(1, n+1):
        if n % i == 0:
            k -= 1
            if k == 0:
                return i
    return -1

# just including the first if statement makes this algorithm faster than 90%!!!!!!!!!
# Speed: faster than 90.85%
# Space: less than 13%
def version3(n,k):
    count = 0
    if k == 1: return 1
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
            if count == k:
                return i
    return -1

if __name__ == "__main__":
    n = 7
    k = 2
    print(version3(n , k))