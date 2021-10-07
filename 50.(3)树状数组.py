class Solution:
    def reversePairs(self,nums):

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
        if size < 2:
            return 0

        s = list(set(nums))

        import heapq
        heapq.heapify(s)
        rank_map = dict()
        rank = 1
        rank_map_size = len(s)
        for _ in range(rank_map_size):
            num = heapq.heappop(s)
            rank_map[num] = rank
            rank += 1
        res = 0

        ft = FenwickTree(rank_map_size)

        for i in range(size-1,-1,-1):
            rank = rank_map[nums[i]]
            ft.update(rank,1)
            res += ft.query(rank-1)
        return res
