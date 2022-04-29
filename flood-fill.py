class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def bfs(graph):
            q = [(sr, sc)]
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited = set()
            
            while q:
                r, c = q.pop(0)
                visited.add((r, c))
                current = graph[r][c]
                
                for dr, dc in directions:
                    r += dr
                    c += dc
                    
                    if r >= 0 and r < len(graph) and c >= 0 and c < len(graph[0]):
                        if graph[r][c] == current and (r, c) not in visited:
                            q.append((r, c))
                    
                    r -= dr
                    c -= dc
                
                image[r][c] = newColor
                
        bfs(image)
            
        return image
