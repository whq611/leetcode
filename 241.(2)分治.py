class Solution:
    def diffWaysToCompute(self, s):
        if s.isdigit():
            return [int(s)]
        res = []
        for i,c in enumerate(s):
            if c in '+-*':
                for left in self.diffWaysToCompute(s[:i]):
                    for right in self.diffWaysToCompute(s[i+1:]):
                        res.append(eval(f'{left}{c}{right}'))
        return res
