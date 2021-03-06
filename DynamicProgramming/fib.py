
def solve_fib(n):
    if n == 1: return 1
    elif n == 2: return 1

    # The whole thing is offset by 2 so in the return I had to offset back to where it is
    # This causes 2 unnecessary computations. Look into it later
    fibs = [1,1]
    for i in range(2, n+2):
        fibs.append(fibs[i - 2] + fibs[i - 1])
        print(fibs)

    return fibs[n-2]

# Uses only 3 variables for optimal space complexity
def solve_fib2(n):
    if n == 1: return 1
    elif n == 2: return 1

#     just remember last two values
    n_1 = 1
    n_2 = 0
    answer = 0

    for i in range(n-1):
        n_2 = n_1
        n_1 = answer
        answer = n_1 + n_2
    return answer


if __name__ == '__main__':

    testcases = [
        3,
        6,
        10,
    ]

    for n in testcases:
        print(f"The {n}th fib is {solve_fib(n)}")
        print(f"The {n}th fib is {solve_fib2(n)}")