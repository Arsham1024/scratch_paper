
def length(s):
    s = s.strip()

    if len(s) == 1:
        return 1

    i = -1
    while s[i] != " ":
        i -= 1
        if len(s) <= abs(i):
            i -= 1
            break

    return abs(i) - 1

# one liner
def version2(s):
    return len(s.split()[-1])

if __name__ == '__main__':
    s = " ba "
    print(length(s))
    print(version2(s))