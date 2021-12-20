
# element = the item to be found
def contains(element):
    for i in elements:
        if i == element:
            return True
    return False

# find duplicates in array
def find_dups():
    seen = set()
    dups = set()

    for i in elements:
        if i in seen:
            dups.add(i)
        seen.add(i)

    return list(dups)

# check if anagram
def is_anagram(s1 , s2):
    return set(s1) == set(s2)

def is_anagram2(s1,s2):
    if len(s1) != len(s2):
        return False

    s1 = list(s1)
    s2 = list(s2)

    for i, letter in enumerate(s1):
        if letter in s2:
            s2.remove(letter)
            continue
        else:
            return False
    return len(s2) == 0

def reverse_string_r(string):
    if len(string) <= 1:
        return string

    return reverse_string_r(string[1:]) + string[0]

def reverse_string_s(string):
    stack = list(string)
    st = ""

    for i in range(len(stack)):
        st += stack.pop()

    return st


if __name__ == "__main__":
    elements = [1,2,3,4,5,6,2,4]

    # if the element contains in the array
    element = 10
    print(f"elements array contains {element}" if contains(element) else f"elements array dose not contain {element}","\n")

    # remove duplicates using set()
    # Done automatically
    print("removed duplicates automatically:" , set(elements),"\n")

    # find the dups
    print("found these duplicates: " , find_dups(),"\n")

    # is anagram
    s1 = "elvis"
    s2 = "lives"
    print(f"{s1} is an anagram of {s2}" if is_anagram(s1,s2) else f"{s1} is NOT an anagram of {s2}")

    # detailed implementation
    s1 = "elvis"
    s2 = "lives"
    print(f"{s1} is an anagram of {s2}" if is_anagram2(s1,s2) else f"{s1} is NOT an anagram of {s2}")

    # reverse string using recursion
    st = "hello"
    print(reverse_string_r(st))

    # reverse string using stack
    print(reverse_string_s(st))

