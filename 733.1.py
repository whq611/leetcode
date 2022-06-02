class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def bfs(image, sr, sc, a, newColor):
            stack = collections.deque([[sr, sc]])
            while stack:
                sr, sc = stack.popleft()
                if 0<=sr<len(image) and 0<=sc<len(image[0]) and image[sr][sc] == a:
                    image[sr][sc] = newColor
                    stack.append([sr-1,sc])
                    stack.append([sr+1,sc])
                    stack.append([sr,sc-1])
                    stack.append([sr,sc+1])
                
            return image
        a = image[sr][sc]
        if a==newColor: return image
        return bfs(image, sr, sc, a, newColor)
