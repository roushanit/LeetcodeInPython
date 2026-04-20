def find_min(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] <= nums[high]:
            high = mid
        else:
            low = mid + 1

    return nums[low]


# Test
nums = [7, 8, 9, 1, 2, 3, 4]
print(find_min(nums))
