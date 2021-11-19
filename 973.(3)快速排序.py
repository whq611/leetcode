class Solution:
    def kClosest(self, points, k):
        def random_select(left, right, k):
            pivot_id = random.randint(left, right)
            pivot = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2
            points[right], points[pivot_id] = points[pivot_id], points[right]
            i = left - 1
            for j in range(left, right):
                if points[j][0] ** 2 + points[j][1] ** 2 <= pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            i += 1
            points[i], points[right] = points[right], points[i]
            # [left, i-1] 都小于等于 pivot, [i+1, right] 都大于 pivot
            if k < i - left + 1:
                random_select(left, i - 1, k)
            elif k > i - left + 1:
                random_select(i + 1, right, k - (i - left + 1))

        n = len(points)
        random_select(0, n - 1, k)
        return points[:k]
