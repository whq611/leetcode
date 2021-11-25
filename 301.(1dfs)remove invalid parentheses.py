class Solution:
    def removeInvalidParentheses(self, s):
        self.ans = set()
        self.min_removed = float("inf")

        def dfs(depth, left, right, removed, cur):
            if depth == len(s):
                if left == right:
                    if removed < self.min_removed:
                        self.min_removed = removed
                        self.ans = {cur}
                    elif removed == self.min_removed:
                        self.ans.add(cur)
            else:
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth + 1, left, right, removed, cur + s[depth])
                else:
                    dfs(depth + 1, left, right, removed + 1, cur)
                    if s[depth] == "(":
                        dfs(depth + 1, left + 1, right, removed, cur + "(")
                    elif s[depth] == ")" and right < left:
                        dfs(depth + 1, left, right + 1, removed, cur + ")")

        dfs(0, 0, 0, 0, "")
        return list(self.ans)
