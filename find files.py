def findfiles(s):
    res = []
    i = 0
    stack1 = []
    stack2 = []
    while i<len(s)-1:
        
        t = 0
        while i<len(s) and s[i] in '\n\t':
            i+=1
            if s[i] == '\t':
                t += 1

        start = i
        while i+1 < len(s) and s[i+1] != '\n':
            i+=1
        stack1.append(s[start:i+1])
        stack2.append(t)
        i += 1
    for i in range(len(stack2)-1):
        if stack2[i]+1 != stack2[i+1]:
            res.append(stack1[i])
    res.append(stack1[-1])
    print(res)
if __name__ == '__main__':
  findfiles("HOME\n\tFILE1\n\tDIR1\n\t\tFILE1\n\t\tFILE2\n\tDIR2\n\t\tSDIR2\n\t\t\tFILE3\n")
