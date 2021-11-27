class Solution:
    def groupString(self,strings):
        for s in strings:
            key = ''
            for i in range(len(s)-1):
                difference = ord(s[i+1]) - ord(s[i])
                key += str(difference % 26) + ','
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        return list(hashmap.values())
