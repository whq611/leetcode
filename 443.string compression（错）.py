class Solution:
    def compress(self, chars):
        a = 1
        res = []
        for i in range(1,len(chars)):
            if chars[i] == chars[i-1]:
                a += 1
            else:
                res.append(chars[i-1])
                if a > 1 and a < 10:
                    res.append(str(a))
                if a >= 10:
                    res.extend(list(str(a)))
                
                a = 1
        if chars[-1] == chars[-2]:
            res.append(chars[-1])
            if a > 1 and a < 10:
                    res.append(str(a))
            if a >= 10:
                    res.extend(list(str(a)))
        else:
            res.append(chars[-1])
        
        return res
