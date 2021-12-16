class Solution:
    def findCircleNum(self, isConnected):
        
        adj_list = {}
        
        for i in range(len(isConnected)):
            neighbors = isConnected[i]
            adj_list[i] = []
            for j in range(len(neighbors)):
                if neighbors[j] == 1:
                    adj_list[i].append(j)
                    
                    
        output = 0
        visited = set()
        q = [0]
        
        for key in adj_list:
            if key not in visited:
                if not q:
                    q.append(key)
                while q:
                    city = q.pop(0)
                    visited.add(city)
                    
                    for neighbor in adj_list[city]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            
                output += 1
                
        return output