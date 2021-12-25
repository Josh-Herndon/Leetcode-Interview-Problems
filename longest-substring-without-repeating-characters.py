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