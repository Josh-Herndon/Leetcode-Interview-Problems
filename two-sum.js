/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    const idxMap = {};
    
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i]
        let val = target - num;
        
        if (val in idxMap) {
            return [i, idxMap[val]]
        }
        
        idxMap[num] = i;
    }
};
