class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ans = -1
        inc = 0
        found = False
        
        while not found and nums:
            mid = len(nums)//2
            
            if nums[mid] == target:
                found = True
                ans = mid + inc
            elif nums[mid] < target:
                inc += len(nums[:mid + 1])
                nums = nums[mid + 1:]
            else:
                nums = nums[:mid]
                
        return ans
