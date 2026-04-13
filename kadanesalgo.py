def maxSubArray(nums):
    n = len(nums)
    maxi = float("-inf")  # Initialize to negative infinity
    total = 0
    
    for i in range(0, n):
        total = total + nums[i]
        maxi = max(maxi, total)
        
        if total < 0:
            total = 0
    
    return maxi

# Example from screenshot
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))  # Output: 6 (subarray [4, -1, 2, 1])
