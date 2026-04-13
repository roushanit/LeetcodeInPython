from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            # skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans
nums = [-1, 0, 1, 2, -1, -4]

obj = Solution()
print(obj.threeSum(nums))        
