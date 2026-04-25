from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            # left neighbor greater
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1

            # right neighbor greater
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1

            else:
                return m

        return -1  # fallback (should never hit)


# 🔥 Run tests
sol = Solution()

print(sol.findPeakElement([1, 2, 3, 1]))       # Expected: 2
print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Expected: 5
print(sol.findPeakElement([1]))                # Expected: 0
print(sol.findPeakElement([5, 4, 3, 2, 1]))    # Expected: 0
print(sol.findPeakElement([1, 2, 3, 4, 5]))    # Expected: 4
