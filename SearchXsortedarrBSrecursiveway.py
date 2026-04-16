def binarySearch(nums, low, high, target):
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearch(nums, mid + 1, high, target)
    else:
        return binarySearch(nums, low, mid - 1, target)


# ---- Test ----
nums = [2, 4, 6, 7, 9, 11, 18, 19]
target = 6

result = binarySearch(nums, 0, len(nums) - 1, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
