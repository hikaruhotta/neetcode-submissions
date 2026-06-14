class TrieNode:
    def __init__(self):
        self.trie = {}
        self.is_word = False
        self.refs = 0

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_root = self.constructTrie(words)
        self.result = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie_root.trie:
                    visited = set([(row, col)])
                    self.findWordsHelper(board, row, col, trie_root.trie[board[row][col]], board[row][col], visited)

        return list(self.result)

    def findWordsHelper(self, board: List[List[str]], row: int, col: int, node: TrieNode, seq: str, visited: Set) -> None:
        if node.refs == 0:
            return
        
        if node.is_word:
            self.result.add(seq)
            node.refs -= 1
        
        for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            next_row, next_col = row + x, col + y
            if self.inbounds(board, next_row, next_col) and (next_row, next_col) not in visited:
                ch = board[next_row][next_col]
                if ch in node.trie:
                    visited.add((next_row, next_col))
                    self.findWordsHelper(board, next_row, next_col, node.trie[ch], seq + ch, visited)
                    visited.remove((next_row, next_col))


    def inbounds(self, board: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])


    def constructTrie(self, words: List[str]) -> TrieNode:
        root = TrieNode()
        for word in words:
            self.addWord(word, root)
        return root

    def addWord(self, word: str, node: TrieNode) -> None:
        node.refs += 1

        if len(word) == 0:
            node.is_word = True
            return
        
        if word[0] not in node.trie:
            node.trie[word[0]] = TrieNode()
        
        self.addWord(word[1:], node.trie[word[0]])
        