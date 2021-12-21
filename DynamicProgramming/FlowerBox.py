
def max_flowerbox(nutrition_values):
    # Special cases where there is a definite answer.
    if len(nutrition_values) == 0:
        return 0
    elif len(nutrition_values) == 1:
        return nutrition_values[0]
    elif len(nutrition_values) == 2:
        return max(nutrition_values)


    # Dynamic programming solution
    else:
        best_sofar = 0 # f(i-2)
        b = 0 # f(i-1)
        for val in nutrition_values:
            best_sofar,b = b, max(best_sofar+val, b)
            print("best so far" , best_sofar)
            print("b", b , "\n")

        return b


if __name__ == "__main__":
    testcases = [
        [3,10,3,1,2],
        [9,10,9],
        [10,9],
        [10],
        []
    ]

    for case in testcases:
        print(f"for test case {case} we get the maximum growth value of {max_flowerbox(case)}")