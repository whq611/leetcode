class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(index,path):
            if len(path)==k:
                res.append(path[:])
                return
            for i in range(index, n-(k-len(path))+2):
                path.append(i)
                dfs(i+1, path)
                path.pop()
        
        res = []
        if k<=0 or k>n:
            return res
        path = []
        dfs(1,path)
        return res
