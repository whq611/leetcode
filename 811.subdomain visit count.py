import collections
class Solution:
    def subdomainVisits(self, cpdomains):
        c = collections.defaultdict(int)
        e = []
        for i in cpdomains:
            a = i.split()
            b = a[1].split('.')
            d = len(b)
            for j in range(d):
                c['.'.join(b[j:])] += int(a[0])
        for i in c:
            e.append(str(c[i]) + ' ' + i)
        return e
