class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(index, total, subset):
            if total == 0:
                result.append(subset.copy())
                return
            
            if total < 0:
                return
            
            for i in range(index, len(candidates)):
                # Skip duplicates
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                # Pruning (important optimization)
                if candidates[i] > total:
                    break
                
                subset.append(candidates[i])
                backtrack(i + 1, total - candidates[i], subset)
                subset.pop()

        backtrack(0, target, [])
        return result


# Run test
obj = Solution()
print(obj.combinationSum2([1,1,1,2,3], 4))
