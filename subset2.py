from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            # include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # exclude nums[i]
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res


# 🔹 Run and test
sol = Solution()
output = sol.subsetsWithDup([1, 2, 2])
print(output)
