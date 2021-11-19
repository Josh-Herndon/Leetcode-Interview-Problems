from collections import OrderedDict

class Solution:
    def topKFrequent(self, words, k):

        freq_map = OrderedDict()
        output = []

        words.sort()

        for word in words:
            if word not in freq_map:
                freq_map[word] = 1
            else:
                freq_map[word] += 1

        while len(output) < k:
            maximum = 0
            for key in freq_map:
                if freq_map[key] > maximum:
                    top_word = key
                    maximum = freq_map[top_word]
            output.append(top_word)
            del freq_map[top_word]

        return output