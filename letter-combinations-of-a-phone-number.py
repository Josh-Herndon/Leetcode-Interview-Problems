class Solution:
    def letterCombinations(self, digits):

        if not digits:
            return []

        output = []
        comb_len = len(digits)

        digit_map = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']
                    }


        q = ['']

        while len(q) > 0:
            s = q.pop(0)

            if len(s) == comb_len:
                output.append(s)
            else:
                for letter in digit_map[digits[len(s)]]:
                    q.append(s + letter)

        return output