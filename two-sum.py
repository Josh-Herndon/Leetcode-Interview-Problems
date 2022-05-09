class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx_map = {}
        
        for i, val in enumerate(nums):
            num = target - val
            
            if num in idx_map:
                return [i, idx_map[num]]
            
            idx_map[val] = i
