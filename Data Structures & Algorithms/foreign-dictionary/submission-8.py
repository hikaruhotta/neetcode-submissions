from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        characters = set()
        for word in words:
            for ch in word:
                characters.add(ch)

        graph = {ch: [] for ch in characters}
        indegree = {ch: 0 for ch in characters}

        print(graph)
        print(indegree)
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            i, j = 0, 0
            while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                i += 1
                j += 1
            
            # lexicologically impossible
            if i < len(word1) and j == len(word2):
                return ""

            if i < len(word1) and j < len(word2):
                graph[word1[i]].append(word2[j])
                indegree[word2[j]] += 1

        result = ""

        queue = deque([])
        visited = set()
        for key, val in indegree.copy().items():
            if val == 0:
                queue.append(key)
                del indegree[key]

        while queue:
            ch = queue.popleft()
            if ch in visited:
                return ""
            
            visited.add(ch)
            result += ch

            for neighbor in graph[ch]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    del indegree[neighbor]
        
        if len(result) == len(characters):
            return result
        
        return ""