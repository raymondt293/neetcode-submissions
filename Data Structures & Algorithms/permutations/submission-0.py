class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        visited = set()
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    path.append(num)
                    backtrack(path)
                    path.pop()
                    visited.remove(num)
        
        backtrack([])
        return res



