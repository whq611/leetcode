class Solution:
    def findNthDigit(self, n):
        digit,start,count = 1,1,9
        while n>count:
            n-=count
            start*=10
            dight+=1
            count=9*start*digit
        num = start+(n-1)//digit
        return int(str(num)[(n-1)%digit])
