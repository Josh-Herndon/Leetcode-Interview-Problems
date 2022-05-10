class Solution:
    def lengthOfLongestSubstring(self, s):
        
        arr = []
        maximum, current = 0, 0
        
        for letter in s:
            if letter in arr:
                current = len(arr)
                index = arr.index(letter)
                arr = arr[index + 1:]
                
            if current > maximum:
                maximum = current
                
            arr.append(letter)
            
        return max(maximum, len(arr))
    
## Solution 2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        idx_map = {}
        low, current, maximum, last = 0, 0, 0, -1
        
        for i, letter in enumerate(s):
            if letter in idx_map:
                current = i - low
                new_pos = idx_map[letter] + 1
                
                low = new_pos if new_pos > low else low
                
            if current > maximum:
                maximum = current
                
            last = i
            idx_map[letter] = i
            
        return max(maximum, last - low + 1)
