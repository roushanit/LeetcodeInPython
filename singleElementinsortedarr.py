
def single_non_duplicate(nums):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        # make mid even
        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            lo = mid + 2
        else:
            hi = mid

    return nums[lo]
    
nums = [1, 1, 2, 3, 3, 4, 4]
print(single_non_duplicate(nums))  # Output: 2    
