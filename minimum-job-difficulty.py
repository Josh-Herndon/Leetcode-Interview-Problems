

class Solution:
    def minDifficulty(self, jobDifficulty, d):
        
        num_jobs = len(jobDifficulty)
        memo = {}
        
        if num_jobs < d:
            return -1
        
        def dp(day, cut):
            print(f'(day, cut) is {(day, cut)}')
            if (day, cut) in memo:
                return memo[(day, cut)]
            if day == 1:
                return max(jobDifficulty[cut:])
            
            maxsofar = 0
            ans = float('inf')
            
            for j in range(cut, num_jobs - day + 1):
                print(f'j is {j}')
                maxsofar = max(maxsofar, jobDifficulty[j])
                print(f'maxsofar is {maxsofar}')
                ans = min(ans, maxsofar + dp(day - 1, j + 1))
                print(f'ans is {ans}')
            
            memo[(day, cut)] = ans
            
            return ans
        
        return dp(d, 0)

days = 3
jobs = [7, 1, 7, 1, 7, 1]

s = Solution()
print(s.minDifficulty(jobs, days))