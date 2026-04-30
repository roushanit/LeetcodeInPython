from typing import List

class Solution:
    def solve(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(subset.copy())
            return
        
        if total > target or index >= len(nums):
            return
        
        # Take current element
        subset.append(nums[index])
        self.solve(index, total + nums[index], subset, nums, target, result)
        
        # Backtrack
        subset.pop()
        
        # Skip current element
        self.solve(index + 1, total, subset, nums, target, result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result


# Test it
obj = Solution()
print(obj.combinationSum([2,3,6,7], 7))
