nums = [-2,1,-3,4,-1,2,1,-5,4]

def version1():
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0], nums[1], nums[1] + nums[0])
    data = [nums[0]]
    maxi = nums[0]

    for i in range(1, len(nums)):
        data.append(max(nums[i], nums[i] + data[i - 1]))
        maxi = max(maxi, data[i])

    return maxi

if __name__ == "__main__":
    print(f"maximum subarray is : {version1()}")