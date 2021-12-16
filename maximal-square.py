class Solution:
    def maximalSquare(self, matrix):
        
        rows, cols = len(matrix), len(matrix[0])
        cache = {}
        
        def fill_cache(r, c):
            
            if r >= rows or c >= cols:
                return 0
            
            if (r, c) not in cache:
                down = fill_cache(r + 1, c)
                right = fill_cache(r, c + 1)
                diag = fill_cache(r + 1, c + 1)
                
                cache[(r, c)] = 0
                if matrix[r][c] == '1':
                    cache[(r, c)] = 1 + min(down, right, diag)
                    
            return cache[(r, c)]
        
        fill_cache(0, 0)
        
        return max(cache.values())**2