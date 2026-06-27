class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.found = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        self._insertHelper(self.root, word)

    def _insertHelper(self, node: TrieNode, word: str):
        if len(word) == 0:
            node.is_end_of_word = True
            return
        
        if word[0] not in node.children:
            node.children[word[0]] = TrieNode()
        
        self._insertHelper(node.children[word[0]], word[1:])

    def search(self, word: str) -> bool:
        node = self._findNode(self.root, word)
        if not node:
            return False
        return node.is_end_of_word

    def prefix(self, word: str) -> bool:
        node = self._findNode(self.root, word)
        return node is not None

    def _findNode(self, node: TrieNode, word: str) -> Optional[TrieNode]:
        if len(word) == 0:
            return node
        
        if word[0] not in node.children:
            return None
        
        return self._findNode(node.children[word[0]], word[1:])

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        char_cell = {}
        for row in range(len(board)):
            for col in range(len(board[0])):
                ch = board[row][col]
                if ch not in char_cell:
                    char_cell[ch] = []
                char_cell[ch].append((row, col))
        
        self.result, self.board = [], board
        for child, child_node in trie.root.children.items():
            if child in char_cell:
                for (row, col) in char_cell[child]:
                    visited = set([(row, col)])
                    self.helper(child_node, row, col, visited, [self.board[row][col]])
        
        return self.result
        
    def helper(self, node: TrieNode, row: int, col: int, visited: Set, path: List[str]):
        if node.is_end_of_word and not node.found:
            self.result.append("".join(path))
            node.found = True
        
        for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nr, nc = row + x, col + y
            if self.inbounds(nr, nc):
                ch = self.board[nr][nc]
                if ch in node.children and (nr, nc) not in visited and node:
                    visited.add((nr, nc))
                    path.append(ch)
                    self.helper(node.children[ch], nr, nc, visited, path)
                    path.pop()
                    visited.remove((nr, nc))

    def inbounds(self, row: int, col: int) -> bool:
        return row >= 0 and row < len(self.board) and col >= 0 and col < len(self.board[0])


        