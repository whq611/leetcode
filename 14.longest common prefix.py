class Solution:
    def longestCommonPrefix(self, strs):
        count = len(strs)
        answer = ''
        lens = len(strs[0])
        if lens == 0 or count == 0:
            return answer
        elif count == 1:
            return strs[0]
        else:
            for i in range(lens):
                for j in range(1,count):
                    if i + 1 > len(strs[j]):
                        answer = answer + strs[0][:i]
                        return answer
                    if strs[0][i] == strs[j][i]:
                        pass
                    else:
                        answer = answer + strs[0][:i]
                        return answer
            answer = answer + strs[0]
            return answer
