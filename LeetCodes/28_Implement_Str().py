import time
def find_string_original(haystack, needle):
    if len(needle) == 0 :
        return 0
    elif len(haystack) == 0:
        return -1

    # Don't need to go all the way to the end becase the needle has some length that it needs to match
    # the last char is gonna have less chars than required.
    for i in range(len(haystack) + len(needle) -1):
        if haystack[i] == needle[0]:
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                elif j == len(needle)-1:
                    return i
    return -1



def find_string(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1

    for i in range(len(haystack) + 1 - len(needle)):
        # some weird shit to make this faster to pass leetcode eventhough time complexity is the same as two for loops
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1

# This version is the fastest in leetcode! wtf? literally not even implemented!
def version2(haystack, needle):
    return haystack.find(needle)


if __name__ == '__main__':
    haystack = "hello"
    needle = 'll'

    start = time.time()
    print(find_string_original(haystack, needle))
    end = time.time()

    print(f"fx1 time : {end - start}")

    start = time.time()
    print(find_string(haystack, needle))
    end = time.time()

    print(f"fx1 time : {end - start}")

    start = time.time()
    print(version2(haystack,needle))
    end = time.time()

    print(f"fx1 time : {end - start}")