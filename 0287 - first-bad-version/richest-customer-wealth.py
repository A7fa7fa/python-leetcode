
def isBadVersion(i:int):
    # [1,2,3,4,5]
    mat = [True, True, True, False, False]

    return not mat[i - 1]

def firstBadVersion(n: int) -> int:    
    
    start = 1
    end = n
    # first element is 1 not 0
    while start < end:
        middle = (start + end) // 2
        print(start, middle, end)
        
        if isBadVersion(middle):
            # middle bad - move left to find first good
            end = middle
        else:
            # all good - move right, first bad version is at least middle + 1
            start = middle + 1

    return start

res= firstBadVersion(5)
print(res)
