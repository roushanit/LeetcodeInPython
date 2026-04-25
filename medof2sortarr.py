from typing import List

class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A)

        while True:
            i = (l + r) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
                
# 🔥 Test cases
sol = Solution()

# 1. Basic case (odd length)
print(sol.findMedianSortedArrays([1, 3], [2]))
# Expected: 2

# 2. Basic case (even length)
print(sol.findMedianSortedArrays([1, 2], [3, 4]))
# Expected: 2.5

# 3. Different sizes
print(sol.findMedianSortedArrays([1, 3, 8], [7, 9, 10, 11]))
# Expected: 8

# 4. One empty array
print(sol.findMedianSortedArrays([], [1]))
# Expected: 1

# 5. Uneven + mixed values
print(sol.findMedianSortedArrays([0, 0], [0, 0]))
# Expected: 0                
