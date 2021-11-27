class Solution:
    def longestPalindrome(self, s):

        res_ind = (None, None)
        res_len = 0

        def find_palindromes(string, res_ind, res_len, even=False):

            for i in range(len(string)):

                if even:
                    l, r = i, i + 1
                else:
                    l, r = i, i

                while l >= 0 and r < len(string) and s[l] == s[r]:

                    if r - l + 1 > res_len:
                        res_ind = (l, r + 1)
                        res_len = r - l + 1

                    l -= 1
                    r += 1

            return res_ind, res_len

        res_ind, res_len = find_palindromes(s, res_ind, res_len)
        res_ind, res_len = find_palindromes(s, res_ind, res_len, even=True)

        return s[res_ind[0]:res_ind[1]]