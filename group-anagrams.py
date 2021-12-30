class Solution:
    def groupAnagrams(self, strs):

        groups = {}
        output = []

        for s in strs:
            key = []

            for letter in s:
                key.append(letter)

            key.sort()
            key = tuple(key)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        for key in groups:
            output.append(groups[key])

        return output