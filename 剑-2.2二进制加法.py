class Solution:
    def addBinary(self, a, b):
        tmp = 0
        res = ''
        a = a[::-1]
        b = b[::-1]
        for i in range(min(len(a),len(b))):
            if a[i] == '0' and b[i] == '0' and tmp == 0:
                res = '0' + res
            elif a[i] == '0' and b[i] == '0' and tmp == 1:
                res = '1' + res
                tmp = 0
            elif a[i] == '1' and b[i] == '1' and tmp == 1:
                res = '1' + res
                tmp = 1
            elif a[i] == '1' and b[i] == '1' and tmp == 0:
                res = '0' + res
                tmp = 1
            elif tmp == 0:
                res = '1' + res
                tmp = 0
            else:
                res = '0' + res
                tmp = 1
        
        if len(a)>len(b):
            for i in range(len(b),len(a)):
                if a[i] == '0' and tmp == 0:
                    res = '0' + res
                elif a[i] == '1' and tmp == 0:
                    res = '1' + res
                elif a[i] == '0' and tmp == 1:
                    res = '1' + res
                    tmp = 0
                else:
                    res = '0' + res
                    tmp = 1
        else:
            for i in range(len(a),len(b)):
                if b[i] == '0' and tmp == 0:
                    res = '0' + res
                elif b[i] == '1' and tmp == 0:
                    res = '1' + res
                elif b[i] == '0' and tmp == 1:
                    res = '1' + res
                    tmp = 0
                else:
                    res = '0' + res
                    tmp = 1
        if tmp == 1:
            res = '1' + res
        return res
