
def solve_fib(n):
    if n == 1: return 1
    elif n == 2: return 1

    fibs = [1,1]
    for i in range(2, n+1):
        fibs.append(fibs[i - 2] + fibs[i - 1])
        print(fibs)

    return fibs[n]

if __name__ == '__main__':

    testcases = [
        3,
        6,
        10,
        20,
        40,
        50
    ]

    for n in testcases:
        print(f"The {n}th fib is {solve_fib(n)}")