
def find_string(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1

    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1

# This version is the fastest in leetcode! wtf? literally not even implemented!
def version2(haystack, needle):
    return haystack.find(needle)


if __name__ == '__main__':
    haystack = "hello"
    needle = 'll'

    print(find_string(haystack, needle))
    print(version2(haystack,needle))