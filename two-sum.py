class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            pair_member = target - nums[i]
            if pair_member in nums[i+1:]:
                index = nums[i+1:].index(pair_member) + len(nums[:i+1])
                return [i, index]