from collections import deque
class Solution:
    def compress(self, chars):
        a = 1
       
        chars = deque(chars)
        for i in range(1,len(chars)):
            if chars[1] == chars[0]:
                a += 1
                chars.popleft()
                
            else:
                chars.append(chars.popleft())
                
                if a > 1 and a < 10:
                    chars.append(str(a))
                if a >= 10:
                    chars.extend(deque(str(a)))
                
                a = 1
        if a == 1:
            chars.append(chars.popleft())
            chars.append(chars[-1])
        else:
            chars.append(chars.popleft())
            if a > 1 and a < 10:
                
                chars.append(str(a))
            if a >= 10:
                chars.extend(deque(str(a)))
        print(list(chars))

        
        return len(list(chars))
