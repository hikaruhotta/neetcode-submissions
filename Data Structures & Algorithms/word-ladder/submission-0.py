import heapq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        graph = {word: [] for word in wordList}
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                word1, word2 = wordList[i], wordList[j]
                diff = 0
                for k in range(len(word1)):
                    if word1[k] != word2[k]:
                        diff += 1
                if diff == 1:
                    graph[word1].append(word2)
                    graph[word2].append(word1)
        
        min_heap = []
        heapq.heappush(min_heap, (1, beginWord))
        visited = set()

        while min_heap:
            length, word = heapq.heappop(min_heap)
            if word in visited:
                continue

            visited.add(word)
            if word == endWord:
                return length
            
            for neighbor in graph[word]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (length + 1, neighbor))
        
        return 0




