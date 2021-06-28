class Solution:
    def addStrings(self, num1, num2):
        d = 0 
        c = []
        if len(num1) <= len(num2):
            j = len(num2) - 1
            for i in range(len(num1)-1,-1,-1):
                c.append(str((int(num1[i])+int(num2[j])+d)%10))
                d = int((int(num1[i])+int(num2[j])+d)%100/10)
                j -= 1
            for q in range(j,-1,-1):
                c.append(str((int(num2[q])+d)%10))
                d = int((int(num2[q])+d)%100/10)
        else:
            i = len(num1) - 1
            for j in range(len(num2)-1,-1,-1):
                c.append(str((int(num1[i])+int(num2[j])+d)%10))
                d = int((int(num1[i])+int(num2[j])+d)%100/10)
                i -= 1
            for q in range(i,-1,-1):
                c.append(str((int(num1[q])+d)%10))
                d = int((int(num1[q])+d)%100/10)
        if d != 0:
            c.append('1')
        c = c[::-1]
        answer = ''.join(c) 
        return answer
