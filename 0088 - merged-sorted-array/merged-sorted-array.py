def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    
    # pointer to last  element in nums1
    pointer1 = m - 1
    # pointer to last  element in nums2
    pointer2 = n - 1
    # pointer to last element in nums 1
    pointerResult = m + n -1


    # as long as first element of nums1 and nums2 are not reached 
    # traverse nums1 backwards and either fill with higher value from current pointer nums1 or nums2
    while pointer1 >= 0 and pointer2 >= 0:

        # compare biggest element of num1 and nums2
        if nums1[pointer1] < nums2[pointer2]:
            # element in nums2 is bigger so add to current last position
            nums1[pointerResult] = nums2[pointer2]
            # set pointer to new last element
            pointer2 -= 1
        else:
            # element in nums1 is bigger so add to current last position
            nums1[pointerResult] = nums1[pointer1]
            # set pointer to new last element
            pointer1 -= 1

        # substract 1 to point to next empty sport in list
        pointerResult -= 1

    # if either pointer of nums1 or nums2 are not at 0 add remaining to front of list
    while pointer1 >= 0:
        nums1[pointerResult] = nums1[pointer1]
        # set pointer to new last element
        pointer1 -= 1
        pointerResult -= 1

    while pointer2 >= 0:
        nums1[pointerResult] = nums2[pointer2]
        # set pointer to new last element
        pointer2 -= 1
        pointerResult -= 1



        
nums1 = [1,2,3,0,0,0]
m= 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)


nums1 = [2,0]
m= 1
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)

nums1 = [4,5,6,0,0,0]
m= 3
nums2 = [1,2,3]
n = 3
merge(nums1, m, nums2, n)
print(nums1)