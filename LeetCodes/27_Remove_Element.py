count = 0
for i, item in enumerate(nums):
    if item == val:
        count += 1
        nums[i] = -1

print(nums.sort(reverse=True))
return len(nums) - count

