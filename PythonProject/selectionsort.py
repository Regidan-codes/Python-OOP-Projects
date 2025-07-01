def smallestitem(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionsort(arr):
    new_arr1 = []
    copied_arr = list(arr)
    for i in range(len(copied_arr)):
        smallest = smallestitem(copied_arr)
        new_arr1.append(copied_arr.pop(smallest))
    return new_arr1


print(selectionsort([5,4,3,2,1]))

