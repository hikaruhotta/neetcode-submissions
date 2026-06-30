class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.ref = 0
        self.is_found = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        self.insertHelper(self.root, word)
    
    def insertHelper(self, node: TrieNode, word: str) -> None:
        node.ref += 1

        if len(word) == 0:
            node.is_word = True
            return
        
        if word[0] not in node.children:
            node.children[word[0]] = TrieNode()
        
        self.insertHelper(node.children[word[0]], word[1:])
    
    def search(self, word: str) -> bool:
        node = self.findNode(self.root, word)
        return node and node.is_word
    
    def prefix(self, word: str) -> bool:
        node = self.findNode(self.root, word)
        return node is not None
    
    def findNode(self, node: TrieNode, word: str) -> Optional[TrieNode]:
        if len(word) == 0:
            return node
        
        if word[0] not in node.children:
            return None
        
        return self.findNode(node.children[word[0]], word[1:])

    def remove(self, word: str) -> None:
        self.removeHelper(self.root, word)
    
    def removeHelper(self, node: TrieNode, word: str) -> None:
        node.ref -= 1

        if len(word) == 0:
            return
        
        self.removeHelper(node.children[word[0]], word[1:])
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

        self.result, self.board = [], board
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in self.trie.root.children:
                    visited = set([(row, col)])
                    path = [board[row][col]]
                    self.dfs(self.trie.root.children[board[row][col]], row, col, path, visited)
        return self.result    
    
    def dfs(self, node: TrieNode, row: int, col: int, path: List[str], visited: set()) -> None:
        if node.ref == 0:
            return

        if node.is_word and not node.is_found:
            word = "".join(path)
            self.result.append("".join(path))
            self.trie.remove(word)
            node.is_found = True

        
        for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nr, nc = row + x, col + y
            if self.inbounds(nr, nc) and self.board[nr][nc] in node.children and (nr, nc) not in visited:
                visited.add((nr, nc))
                path.append(self.board[nr][nc])
                self.dfs(node.children[self.board[nr][nc]], nr, nc, path, visited)
                path.pop()
                visited.remove((nr, nc))

    def inbounds(self, row: int, col: int) -> bool:
        return row >= 0 and row < len(self.board) and col >= 0 and col < len(self.board[0])


        