nums = [5,4,-1,7,8]
target = 12

def version1():
    for i in range(len(nums) - 1):
        sum = 0
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == "__main__":
    print(version1())