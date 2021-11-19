class Solution:
    def mostCommonWord(self, paragraph, banned):

        symbols = ['!', '?', "'", ',', ';', '.', '"']
        word_count = {}
        maximum = 0

        for i in range(len(paragraph)):

            if paragraph[i] in symbols:
                paragraph = paragraph[:i] + ' ' + paragraph[i + 1:]

        for word in paragraph.split():

            word = word.lower()

            if word not in banned:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1

                if word_count[word] > maximum:
                    ans = word
                    maximum = word_count[word]

        return ans