class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        n = len(t)
        m = len(s)
        
        if n > m:
            return ''
        
        indices = []
        start_stop = []
        
        for letter in t:
            indices.extend([x[0] for x in enumerate(s) if x[1] == letter])
            
        indices.sort()
            
        count = 1
        for i in range(1, len(indices)):
            if count == 1:
                start = indices[i-1]
            
            count += indices[i] - indices[i-1]
            
            if count >= n:
                start_stop.append((start, indices[i]))
                count = 1

        start_stop_len = len(start_stop)
        times_removed = 0
        minimum = float("inf")
        for i in range(start_stop_len):
            start, stop = start_stop[i-times_removed]

            letter_pos = 0
            while letter_pos < n:
                if t[letter_pos] not in s[start:stop + 1]:
                    start_stop.remove((start, stop))
                    times_removed += 1
                    break

                letter_pos += 1
            
            if (start, stop) in start_stop:
                if stop - start + 1 < minimum:
                    minimum = stop - start + 1
                else:
                    start_stop.remove((start, stop))
                    times_removed += 1
                
        if not start_stop:
            return ''
        
        start = start_stop[0][0]
        stop = start_stop[0][1]
        
        return s[start:stop + 1]

s = "ADOBECODEBANC"
t = "ABC"

a = Solution()
print(a.minWindow(s, t))