def plus1(digits):
    first_i = -1
    length = len(digits)

    if digits[-1] != 9:
        digits[-1] += 1
        return digits

    for i in reversed(range(len(digits))):
        if digits[i] == 9:
            digits[i] = 0
            if i == 0:
                digits[i] = 1
                digits.append(0)
                return digits
            continue

        elif digits[i] != 9:
            digits[i] += 1
            return digits

    return digits

if __name__ == '__main__':
    number = [[9,9,9,9,9,9],
              [1],
              [1,2,3,4],
              [2,9],
              [9],
              ]

    for i in number:
        print(plus1(i))