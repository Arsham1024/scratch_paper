# Anagram
from collections import Counter


def version1(s, t):
    return sorted(s) == sorted(t)

def version2(s , t):
    s = Counter(s)
    t = Counter(t)
    print(s, t)
    return True if s == t else False

if __name__ == '__main__':
    testcase = [
        ["arsham" , "aashram"],
        ["hello", "hello"],
        ["Carr" , "carr"],
        ["car", "rat"],
        ["rat" , "tar"]
    ]

    for i in testcase:
        # print(version1(i[0], i[1]))
        # print(version2(i[0], i[1]))