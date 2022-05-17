class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1 if x > 0 else -1
        x = str(abs(x))
        reverse_x = ''
        
        for i in range(len(x) - 1, -1, -1):
            reverse_x += x[i]
            
        reverse_x = sign*int(reverse_x)
        
        if reverse_x >= -2**31 and reverse_x <= 2**31 - 1:
            return reverse_x
        else:
            return 0
