romans = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

s = "MCMXCIV"
numbers = []


# get the number value of each letter and append to the array for processing
for i in s:
    numbers.append(romans.get(i.upper()))

print(numbers)

def logic(numbers):
    number = 0
    # Case of one letter numbers
    if len(numbers) < 2:
        return numbers[0]

    for i in range(len(numbers)):
        if numbers[i] == 5 and i > 0 and numbers[i-1] == 1:
            # Just did the math because it would have already added 1 so just add 3 more
            number += 3
        elif numbers[i] == 10 and i > 0 and numbers[i-1] == 1:
            number += 8
        elif numbers[i] == 50 and i > 0 and numbers[i-1] == 10:
            number += 30
        elif numbers[i] == 100 and i > 0 and numbers[i-1] == 10:
            number += 80
        elif numbers[i] == 500 and i > 0 and numbers[i-1] == 100:
            number += 300
        elif numbers[i] == 1000 and i > 0 and numbers[i - 1] == 100:
            number += 800
        # no special case here
        else:
            number += numbers[i]

    return number

print(logic(numbers))

