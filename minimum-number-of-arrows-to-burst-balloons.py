class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda coords: coords[0])
        arr = [points[0]]
        output = len(points)
        
        for start, end in points[1:]:
            last_end = arr[-1][1]
            if start <= last_end:
                output -= 1
                arr[-1] = [arr[-1][0], min(end, last_end)]
            else:
                arr.append([start, end])
                
        return output
