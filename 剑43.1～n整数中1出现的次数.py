class Solution:
    def countDigitOne(self, n):
        digit = 1
        res = 0
        high,low,cur = n//10,0,n%10
        while high!=0 or cur!=0:
            if cur==0:
                res+=high*digit
            elif cur==1:
                res+=high*digit+low+1
            else:
                res+=(high+1)*dight
            low += cur*digit
            cur = high%10
            high//=10
            digit*=10
        return res
