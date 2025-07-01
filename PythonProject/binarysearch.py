def binarysearch(arr, item):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid+1
        else:
            high = mid-1
    return None
arr1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(binarysearch(arr1, 15))
