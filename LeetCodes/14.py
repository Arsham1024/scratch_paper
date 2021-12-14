strs = ["Arsham","Arshaaam","Armin"]

# speed: faster than 35%
# space: less than 56%
def version1():
    # return the smallest element's index
    def smallest():
        smallest = len(strs[0])
        index = 0
        for i in strs[1:]:
            if len(i) < smallest:
                index = strs.index(i)
        return index


    def hello(strs , smallest):
        def find():
            for j, letter in enumerate(strs[smallest]):
                buffer = letter
                for i in range(len(strs)):
                    if buffer == strs[i][j]:
                        continue

                    else:
                        return j
        j = find()
        if j == None:
            return str(strs[smallest])
        elif j > 0:
            return str(strs[0][:j])
        else:
            return ""


    print(hello(strs, smallest()))

# speed: faster than 28%
# space: less than 56%
def version2():
    LCP = ""
    for i in range(len(strs[0])):
        for s in strs:
            # No need to find the shortest just check if the i == len(s) current string if it is then that string
            # is the shortest of the bunch. The second condition checks similarity of each letter.
            if i == len(s) or s[i] != strs[0][i]:
                return LCP
        LCP += strs[0][i]
    return LCP

if __name__ == "__main__":
    version2()
