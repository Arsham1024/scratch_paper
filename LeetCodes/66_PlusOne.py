def plus1(digits):

    # The first case where the number on the least sig digit is not 9
    # 1-8 numbers can be +1 with no implications on the rest of the digits
    if digits[-1] != 9:
        digits[-1] += 1
        return digits

    # traverse through the list in reverse order so we can logically assess the numbers
    for i in reversed(range(len(digits))):
        # if the current number is 9
        # check if this number is the last number! in that case make the current number 1 and append one 0 to the end
        # This way we make the number bigger.

        if digits[i] == 9:
            if i == 0:
                digits[i] = 1
                digits.append(0)
                return digits
            # if this index is not the end then just make the number 0 and continue to the next digit
            # until we get to a digit that is less than 9 or end of the digits
            digits[i] = 0
            continue

        # if next digit is not 9 then just add one to it like before
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