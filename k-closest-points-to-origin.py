from math import sqrt

class Solution:
    def kClosest(self, points, k):
        
        distance_map = {}
        ans = []
        
        for point in points:
            dist = sqrt(point[0]**2 + point[1]**2)
            if dist not in distance_map:
                distance_map[dist] = []
            distance_map[dist].append(point)
        
        distances = list(distance_map.keys())
        distances.sort()
        
        for distance in distances:
            ans.extend(distance_map[distance])
            if len(ans) == k:
                break
            
        return ans

