
nums1 = [4,9,5]
nums2 = [9,9]

def intersection():
    intersect = []

    for i in nums1:
        if i in nums2:
            intersect.append(i)
            nums2.pop(nums2.index(i))

    return intersect


if __name__ == "__main__":
    print(intersection())