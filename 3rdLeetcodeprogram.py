import math
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = Counter()
        ans = l = 0
        for r, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans

# Testing the function
solution = Solution()

# Test cases
test_cases = ["abcabcbb", "bbbbb", "pwwkew", "", "dvdf", "a", "abcdef"]

for test in test_cases:
    print(f'Input: "{test}" → Output: {solution.lengthOfLongestSubstring(test)}')

