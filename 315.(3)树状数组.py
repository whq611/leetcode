class Solution:
    def countSmaller(self,nums):
        class FenwickTree:
            def __init__(self,n):
                self.size = n
                self.tree = [0 for _ in range(n+1)]

            def __lowbit(self,index):
                return index & (-index)

            def update(self,index,delta):
                while index <= self.size:
                    self.tree[index] += delta
                    index += self.__lowbit(index)

            def query(self,index):
                res = 0
                while index > 0:
                    res += self.tree[index]
                    index -= self.__lowbit(index)
                return res

        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        s = list(set(nums))

        s_len = len(s)

        import heapq
        heapq.heapify(s)

        rank_map = dict()
        rank = 1
        for _ in range(s_len):
            num = heapq.heappop(s)
            rank_map[num] = rank
            rank += 1

        fenwick_tree = FenwickTree(s_len)
        res = [None for _ in range(size)]
        for index in range(size-1, -1, -1):
            rank = rank_map[nums[index]]
            fenwick_tree.update(rank,1)
            res[index] = fenwick_tree.query(rank-1)
        return res
        
