from collections import deque

class TrieNode:

    def __init__(self):
        self.word_index = -1
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, index):
        curr = self.root
        for ch in s:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word_index = index
    
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
        self.res = set()

        for i, word in enumerate(words):
            trie.insert(word, i)

        self.dfs(board, trie)
        return [words[index] for index in self.res]

    def dfs(self, board: List[List[str]], trie: Trie):
        queue = deque()

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie.root.children:
                    self.dfsHelper(board, trie.root.children[board[row][col]], set([(row, col)]), row, col)

    def dfsHelper(self, board: List[List[str]], trieNode: TrieNode, visited: Set, row: int, col: int) -> Set[int]:
        if trieNode.word_index != -1:
            self.res.add(trieNode.word_index)

        for i, j in [
            (0, -1), (-1, 0), (0, 1), (1, 0)
        ]:
            next_row, next_col = row + i, col + j
            if self.inBounds(board, next_row, next_col) and (next_row, next_col) not in visited and board[next_row][next_col] in trieNode.children:
                visited.add((next_row, next_col))
                self.dfsHelper(board, trieNode.children[board[next_row][next_col]], visited, next_row, next_col)
                visited.remove((next_row, next_col))
                             
        
    def inBounds(self, board: List[List[str]], row: int, col: int) -> bool:
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])
        


        