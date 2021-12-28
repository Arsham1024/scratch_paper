
def removeelements(nums, val):
    count = 0
    for i, item in enumerate(nums):
        if item == val:
            count += 1
            nums[i] = -1

    print(nums.sort(reverse=True))
    return len(nums) - count

if __name__ == '__main__':
    list = [0,1,2,2,3,0,4,2]
    val = 2
    print(removeelements(list, val))