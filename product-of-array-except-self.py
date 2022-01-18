class Solution:
    def productExceptSelf(self, nums):

        output = [1]
        nums_len = len(nums)

        for i in range(nums_len - 1):
            output.append(nums[i] * output[-1])

        prev = 1
        for j in range(nums_len - 1, 0, -1):
            prev *= nums[j]
            output[j - 1] *= prev

        return output