class Solution:
    def isNumber(self,s):
        seen_digit = seen_exponent = seen_dot = False
        for i,c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c == {'+','-'}:
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            elif c in {'e','E'}:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == '.':
                if seen_exponent or seen_dot:
                    return False
            else:
                return False
        return seen_digit
                
