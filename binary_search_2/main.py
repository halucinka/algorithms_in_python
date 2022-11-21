def binary_search(nums, k):
    left = 0
    right = len(nums)-1

    while left < right:
        mid = left + (right - left + 1)//2
        if k < nums[mid]:
            right = mid -1
        else:
            left = mid
        if len(nums) > left and nums[left] == k:
            return left
    return -1


def binary_search_3ifs(nums, k):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left + (right - left + 1)//2
        if k < nums[mid]:
            right = mid -1
        elif nums[mid] < k:
            left = mid + 1
        else:
            return mid
    return -1