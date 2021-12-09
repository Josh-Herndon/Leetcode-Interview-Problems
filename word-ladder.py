from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        neighbors = defaultdict(list)
        pattern_map = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i + 1:]}'
                neighbors[pattern].append(word)
                pattern_map[word].append(pattern)
                
        visited = set(beginWord)
        output = 1
        q = [beginWord]

        while q:
            for _ in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return output
                    
                for pattern in pattern_map[word]:
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                    
            output += 1

        return 0