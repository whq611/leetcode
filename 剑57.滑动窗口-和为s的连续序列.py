def findContinuousSequence(self, target):
    i,j = 1,1
    summ = 0
    res = []
    while i<=target//2:
        if summ<target:
            summ+=j
            j+=1
        elif summ>target:
            summ-=i
            i+=1
        else:
            arr = list(range(i,j))
            res.append(arr)
            summ-=i
            i+=1
    return res
