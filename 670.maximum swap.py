class Solution:
    def maximumSwap(self, num):
        num = str(num)
        max_num = sorted(num)[::-1]
        a,b = 0,0
        for i in range(len(num)):
            if num[i] != max_num[i]:
                a = num[i]
                num = num[:i] + max_num[i] + num[i+1:]
                b = max_num[i]
                break

        if a or b:
            for i in range(len(num))[::-1]:
                if num[i] == b:
                    num = num[:i] + a + num[i+1:]
                    break
        return int(num)
