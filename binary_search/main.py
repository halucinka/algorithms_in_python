# returns index of the element or -1 if not found
def binary_search(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if x == arr[mid]:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid -1
    return -1


# returns index of the element or -1 if not found
def binary_search_optimized(arr, x):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left + 1) // 2
        if arr[mid] > x:
            right = mid - 1
        else:
            left = mid
    # performs equality check only once, at the end
    if len(arr) > left and arr[left] == x:
        return left
    return -1
# returns index of the element where it would be inserted in array


def find_index(arr, x):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left +1) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left
