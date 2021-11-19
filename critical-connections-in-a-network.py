
class Solution:
    def criticalConnections(self, n, connections):
        
        graph = {}
        visited = set()
        timestamp = [0]*n
        time = 0
        output = []
        
        for a, b in connections:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            
            graph[a].append(b)
            graph[b].append(a)
            
        
        def dfs(graph, visited, timestamp, time, node, prev):
           visited.add(node)
           timestamp[node] = time
           low = timestamp[node]
           time += 1

           for v in graph[node]:

               if v == prev:
                   continue
                
               if v not in visited:
                   dfs(graph, visited, timestamp, time, v, node)

               timestamp[node] = min(timestamp[node], timestamp[v])

               if timestamp[v] > low:
                   output.append([node, v])


        dfs(graph, visited, timestamp, time, 0, -1)

        return output
        
s = Solution()

connections = [[0,1],[1,2],[2,0],[1,3]]
n = 4

print(s.criticalConnections(n, connections))