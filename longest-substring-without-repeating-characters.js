/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    
    const idxMap = {};
    var [low, current, maximum, last] = [0, 0, 0, -1];
    
    for (let i = 0; i < s.length; i++) {
        let letter = s[i];
        
        if (letter in idxMap) {
            current = i - low;
            let newPos = idxMap[letter] + 1;
            
            low = newPos > low ? newPos: low;
        }
        
        if (current > maximum) {
            maximum = current;
        }
        
        last = i;
        idxMap[letter] = i;
    }
    
    return Math.max(maximum, last - low + 1)
};
