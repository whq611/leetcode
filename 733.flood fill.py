class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(image, sr, sc, a, newColor):
            if 0<=sr<len(image) and 0<=sc<len(image[0]) and image[sr][sc] == a:
                image[sr][sc] = newColor
                dfs(image, sr-1, sc, a, newColor)
                dfs(image, sr+1, sc, a, newColor)
                dfs(image, sr, sc-1, a, newColor)
                dfs(image, sr, sc+1, a, newColor)
                return image
        a = image[sr][sc]
        if a==newColor: return image
        return dfs(image, sr, sc, a, newColor)
