

def setPointers(arr: list, num: int, mid: int, start: int, end: int) -> tuple:
    if arr[mid] > num:
        end = mid - 1
    else:
        start = mid + 1
    return start, end


def findIdxBinarySearch(arr: list, num: int) -> int:

    result = -1
    if not arr:
        return result

    start = 0
    end = len(arr)

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == num:
            return mid
        start, end = setPointers(
            arr=arr, num=num, mid=mid, start=start, end=end)
    return result


size = 10000000
arr = [i for i in range(size)]

print(findIdxBinarySearch(arr=arr, num=6))
print(findIdxBinarySearch(arr=arr, num=15318))
print(findIdxBinarySearch(arr=arr, num=99999))
print(findIdxBinarySearch(arr=arr, num=1))
print(findIdxBinarySearch(arr=arr, num=3))
