# basically fib

def number_of_ways(steps):
    two = 1
    one = 1

    # need to calculate n-1 times
    for i in range(n-1):
        temp = one
        one = one+two
        two = temp
    return one


if __name__ == '__main__':
    n = 5
    print(number_of_ways(n))