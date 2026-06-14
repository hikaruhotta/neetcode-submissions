from collections import deque

class TrieNode:

    def __init__(self):
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        curr = self.root
        for ch in s:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
    
    def startsWith(self, s):
        curr = self.root
        for ch in s:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        max_len = max([len(word) for word in words])
        
        self.bfs(board, trie, max_len)

        res = []
        for word in words:
            if trie.startsWith(word):
                res.append(word)
        
        return res

    def bfs(self, board: List[List[str]], trie: Trie, max_len: int):
        queue = deque()

        for row in range(len(board)):
            for col in range(len(board[0])):
                queue.append(([(row, col)]))

        while queue:
            path = queue.popleft()
            word = [board[row][col] for (row, col) in path]

            trie.insert(word)

            if len(path) >= max_len:
                continue

            row, col = path[-1]

            for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_row, new_col = row + i, col + j
                if self.inBounds(board, new_row, new_col) and (new_row, new_col) not in path:
                    new_path = path + [(new_row, new_col)]
                    queue.append(new_path)
    
    def inBounds(self, board: List[List[str]], row: int, col: int) -> bool:
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])
        


        