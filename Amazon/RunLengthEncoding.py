
def encode(s):
    result = ""
    length = len(s)
    count = 0 # number of same letters, flush everytime
    for i in range(length):
        if s[i] != s[length-1] and s[i] == s[i+1]:
            count += 1

        else:
            result + str(count) + str(s[i])
            print(count)

    return result





if __name__ == "__main__":
    s = "aa"
    print(encode(s))