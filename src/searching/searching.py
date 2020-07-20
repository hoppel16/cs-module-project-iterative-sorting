def linear_search(arr, target):
    # Your code here
    steps = 0
    for elem in arr:
        if elem is target:
            return steps
        steps += 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (high + low) // 2
        if target is arr[mid]:
            return mid
        if target < arr[mid]:
            high = mid - 1
        if target > arr[mid]:
            low = mid + 1

    return -1  # not found
