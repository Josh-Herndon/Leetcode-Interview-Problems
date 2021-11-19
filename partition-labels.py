class Solution:
    def partitionLabels(self, s):

        letters = []
        substrings = [s[0]]
        min_max = {}
        seen = set()

        for letter in s:
            
            letters.append(letter)

        for letter in letters:

            if letter not in seen:
                indices = [x[0] for x in enumerate(letters) if x[1] == letter]
                min_max[letter] = (min(indices), max(indices))
            
            seen.add(letter)

        current_min = -1
        current_max = -1
        for letter in min_max:

            minimum = min_max[letter][0]
            maximum = min_max[letter][1]

            if minimum not in range(current_min, current_max + 1): 
                current_min = minimum
            
            if maximum not in range(current_min, current_max + 1):
                current_max = maximum

            if current_max >= current_min:
                if substrings[-1] in s[current_min:current_max+1]:
                    substrings.remove(substrings[-1])
                substrings.append(s[current_min:current_max+1])
        
        result = [len(substring) for substring in substrings]

        return result

sol = Solution()
s = "ababcbacadefegdehijhklij"
#s = "abaca"

print(sol.partitionLabels(s))