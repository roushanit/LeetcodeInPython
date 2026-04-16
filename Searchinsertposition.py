def searchInsert(nums, target):
    low, high = 0, len(nums) - 1
    ans = len(nums)

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
    

target = 16

print(searchInsert([1,3,4,5,8,9,14,15,19,20,21],16))
