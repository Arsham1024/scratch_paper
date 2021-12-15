nums = [-92,-333,255,994,36,242,49,-591,419,-432,-73,41,93,654,-20,40,929,-492,432,72,796,795,930,901,-468,890,146,829,932,-585,721,-83,-719,-146,-750,-196,-94,-352,-851,375,-507,-122,-850,-564,372,-379,606,-749,838,592,-683]

def version1():
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Very celever solution
# This is the fastest.
# List(set(nums)) removes duplicates if there are any then the length of it compared to original length would have changed.
def version2():
    if len(list(set(nums))) == len(nums):
        return False
    else:
        return True

if __name__ == "__main__":
    print(version2())