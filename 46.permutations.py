class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(0, len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
        
        res = []
        if not nums:
            return res
        path = []
        dfs(path)
        return res
