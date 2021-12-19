


def merge():
    nums1 = [0]
    m = 0

    nums2 = [2]
    n = 1
# case where num2 is empty no change in num1
# case where num1 is empty

    if m < 1:
        nums1 = nums1.copy()

# Most common case
    for i,item in enumerate(nums2):
        nums1[i+m] = item

    # SORT THE ARRAY AT THE END.
    print(nums1)
    nums1.sort()



if __name__ == "__main__":
    print(merge())