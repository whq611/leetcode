class Solution:
    def shipWithinDays(self, weights, days):
        def ship(weights,d,days):
            c = 0
            for i in weights:
                
                if (c + i) <= d:
                    c += i
                else:
                    days -= 1
                    if days == 0:
                        return 0
                    c = i
                
            return 1
        
        a = sum(weights)
        if a % days == 0:
            b = int(a / days)
        else:
            b = int(a // days + 1)
        d = b
        while ship(weights,d,days) == 0:
            d += 1
        else:
            return max(d,max(weights))
