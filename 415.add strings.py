class Solution:
    def addStrings(self, num1, num2):
        a,b = list(num1)[::-1],list(num2)[::-1]
        length = min(len(a),len(b))
        c = []
        d = 0
        for i in range(length):
            c.append(str((int(a[i])+int(b[i])+d)%10))
            if int(a[i]) + int(b[i]) + d > 9:
                d = 1
            else:
                d = 0
        if len(a) >= len(b):
            for i in range(length,len(a)):
                c.append(str((int(a[i])+d)%10))
                d = int((int(a[i])+d)%100/10)
        else:
            for i in range(length,len(b)):
                c.append(str((int(b[i])+d)%10))
                d = int((int(b[i])+d)%100/10)
        if d != 0:
            c.append('1')
        c = c[::-1]
        answer = ''.join(c) 
        return answer
