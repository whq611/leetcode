class SparseVector:
    def __init__(self,nums):
        self.nonzeros = {}
        for i,n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n
    def dotProduct(self,vec):
        for i,n in self.nonzeros.items():
            if i in vec.nonzeros.items():
                result += n*vec.nonzeros[i]
        return result
