from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        max_len = max([len(word) for word in words])
        
        edges = set()

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    edges.add((word1[j], word2[j]))
                    break
        
        chars = set()
        for word in words:
            for ch in word:
                chars.add(ch)
        
        adj = {}
        for char in chars:
            adj[char] = set()

        in_degree = {ch: 0 for ch in chars}
        
        for u, v in edges:
            adj[u].add(v)
            in_degree[v] += 1

        result = []
        
        queue = deque([ch for ch in chars if in_degree[ch] == 0])

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) < len(chars):
            return ""

        return "".join(result)

