class Solution:
    def lengthLongestPath(self, s):
        ans = 0
        stack = []
        running_sum = 0
        i = 0
        while i < len(s):
            tabs = 0
            while i<len(s) and s[i] in '\n\t':
                i += 1
                if s[i] == '\t':
                    tabs += 1
            while len(stack)>tabs:
                running_sum -= stack.pop()
            start = i
            is_file = False
            while i+1 < len(s) and s[i+1] != '\n':
                if s[i] == '.':
                    is_file = True
                i += 1
            stack.append(i-start+1)
            running_sum += i-start+1
            if is_file:
                ans = max(ans,running_sum+len(stack)-1)
            i += 1
        return ans
