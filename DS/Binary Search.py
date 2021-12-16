
# imagine different inputs and outputs and edge cases
# communicate ideas
# convert thoughts in code
# code should be readable
# approach to solve

# sorted list of numbers
import math

nums = [1,2,3,4,5,6,7,8,9,12,14,15,17]

def find_number(query, arr):
    middle = find_middle(arr)
    print(middle)

    if (middle == query):
        print("found")
        return nums.index(middle)
    elif(middle > query):
        return find_number(query, arr[:arr.index(middle)])
    elif(middle<query):
        return find_number(query, arr[arr.index(middle)+1:])
    else:
        return "index not found"


def find_middle(nums):
    middle = math.floor(len(nums)/2)
    if len(nums) >  middle:
        return "index not found"
    else:
        return nums[middle]

if __name__ == "__main__":
    query = 0
    print(find_number(query, nums))