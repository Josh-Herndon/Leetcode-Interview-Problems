class Solution:
    def trap(self, height):

        output = 0
        max_left = 0
        max_right = max(height)
        arr_len = len(height)

        for i in range(arr_len):
            block = height[i]

            if i + 1 < arr_len:
                if block > max_left:
                    max_left = block
                if block == max_right:
                    max_right = max(height[i+1:])
                water_block = min(max_left, max_right) - block

                if water_block > 0:
                    output += water_block
                    
        return output   