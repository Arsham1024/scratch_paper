strs = ["Arsham","Arshaaam"]

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