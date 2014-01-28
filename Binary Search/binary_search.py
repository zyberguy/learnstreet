def binarySearch(arr, val):
    lo = 0
    hi = len(arr)-1
    ctr = 0
    while lo <= hi:
        mid = (lo+hi)/2
        ctr+=1
        if arr[mid] < val:
            lo = mid + 1
        elif arr[mid] > val:
            hi = mid - 1
        else:
            return (mid,ctr)
    return (-1 ,ctr)