class Solution:
    def maximumSwap(nums):
        num_str = str(num)
        digit_last_index = [None for _ in range(10)]
        for i,digit in enumerate(num_str):
            digit_last_index[int(digit)] = i
        for i,digit in enumerate(num_str):
            for index in range(9,int(digit),-1):
                if digit_last_index[index] != None and digit_last_index[index]>i:
                    return int(num_str[:i]+str(index)+num_str[i+1:digit_last_index[index]]+num_str[i]+num_str[digit_last_index[index]+1:])
        return num
