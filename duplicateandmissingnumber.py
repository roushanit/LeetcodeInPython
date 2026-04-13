def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums))  # Output: 8



def findDuplicate(nums):
    # Phase 1: Detect cycle (find meeting point)
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]          # Move 1 step
        fast = nums[nums[fast]]    # Move 2 steps
        if slow == fast:
            break
    
    # Phase 2: Find cycle entry point (the duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# Examples
print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(findDuplicate([3, 1, 3, 4, 2]))  # Output: 3
print(findDuplicate([2, 2, 2, 2, 2]))  # Output: 2
