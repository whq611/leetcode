class Solution:
    def KClosest(self,points,k):
        heap = []
        for (x,y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heapqpushpop(heap,(dist,x,y))
            else:
                heapq.heapqpush(heap,(dist,x,y))
        return [(x,y) for (dist,x,y) in heap]
