class Solution:
    def canMakeBouq(self, bloomDay, mid, k):
        bouqCount = 0
        consecutive = 0

        for day in bloomDay:
            if day <= mid:
                consecutive += 1
                if consecutive == k:
                    bouqCount += 1
                    consecutive = 0
            else:
                consecutive = 0

        return bouqCount

    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)

        # Important edge case
        if m * k > n:
            return -1

        start = 0
        end = max(bloomDay)
        minDays = -1

        while start <= end:
            mid = start + (end - start) // 2

            if self.canMakeBouq(bloomDay, mid, k) >= m:
                minDays = mid
                end = mid - 1
            else:
                start = mid + 1

        return minDays
        
        
bloomDay = list(map(int, input("Enter bloom days: ").split()))
m = int(input("Enter m: "))
k = int(input("Enter k: "))

sol = Solution()
print("Minimum Days:", sol.minDays(bloomDay, m, k))        
