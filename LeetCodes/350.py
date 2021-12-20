
nums1 = [4,9,5]
nums2 = [9,9]

def version1():
    intersect = []

    for i in nums1:
        if i in nums2:
            intersect.append(i)
            nums2.pop(nums2.index(i))

    return intersect

def version2():
    intersect = []

    nums1.sort()
    nums2.sort()

    i, j = 0,0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            intersect.append(nums1[i])
            i+=1
            j+=1

        elif nums1[i] < nums2[j]:
            i+=1
        else:
            j+=1

    return intersect


if __name__ == "__main__":
    print(version2())