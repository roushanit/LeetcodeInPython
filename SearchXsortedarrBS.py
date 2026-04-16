def binarySearch(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ---- Test it ----
nums = [2, 4, 6, 7, 9, 11, 18, 19]
target = 13

result = binarySearch(nums, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not available")
