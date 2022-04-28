class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s = [letter for letter in s]
        t = [letter for letter in t]
        
        s.sort()
        t.sort()
        
        if s == t:
            return True
        else:
            return False
