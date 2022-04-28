import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alphanum = string.ascii_lowercase + '0123456789'
        new_s = ''
        reverse_s = ''
        
        for letter in s:
            if letter.lower() in alphanum:
                new_s += letter.lower()
                
        for i in range(len(new_s) - 1, -1, -1):
            reverse_s += new_s[i]
        
        if new_s == reverse_s:
            return True
        
        return False
