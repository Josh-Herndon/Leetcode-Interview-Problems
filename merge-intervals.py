class Solution:
    def merge(self, intervals):
        
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            
            if start <= last_end:
                output[-1] = [output[-1][0], max(end, last_end)]
            else:
                output.append([start, end])
                
        return output