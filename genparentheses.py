from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, s):
            if len(s) == 2 * n:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        dfs(0, 0, "")
        return res


# ---- Run and check output ----
if __name__ == "__main__":
    sol = Solution()
    
    n = 3  # change this value to test
    output = sol.generateParenthesis(n)
    
    print(f"Input: n = {n}")
    print("Output:")
    print(output)
