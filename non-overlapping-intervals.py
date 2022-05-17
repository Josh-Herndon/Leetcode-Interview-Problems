class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda i: i[0])
        arr = [intervals[0]]
        output = 0
        
        for start, end in intervals[1:]:
            last_end = arr[-1][1]
            if start < last_end:
                output += 1
                arr[-1] = [arr[-1][0], min(end, last_end)]
            else:
                arr.append([start, end])
                
        return output
