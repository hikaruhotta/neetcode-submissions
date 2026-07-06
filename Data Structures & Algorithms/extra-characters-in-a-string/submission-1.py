class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        self.insertHelper(self.root, word)

    def insertHelper(self, node: TrieNode, word: str) -> None:
        if len(word) == 0:
            node.is_word = True
            return
        
        if word[0] not in node.children:
            node.children[word[0]] = TrieNode()
        
        self.insertHelper(node.children[word[0]], word[1:])

    def search(self, word: str) -> bool:
        node = self.findNode(self.root, word)
        return node is not None and node.is_word

    def prefix(self, word: str) -> bool:
        node = self.findNode(self.root, word)
        return node is not None

    def findNode(self, node: TrieNode, word: str) -> Optional[TrieNode]:
        if len(word) == 0:
            return node
        
        if word[0] not in node.children:
            return None
        
        self.findNode(node.children[word[0]], word[1:])

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.trie = Trie()
        for word in dictionary:
            self.trie.insert(word)
        self.s = s

        self.cache = {}

        return self.helper(0)
    
    def helper(self, index: 0) -> int:
        if index == len(self.s):
            return 0

        if index in self.cache:
            return self.cache[index]
        
        j = index
        node = self.trie.root
        results = []

        while j < len(self.s):
            if self.s[j] not in node.children:
                break
            node = node.children[self.s[j]]
            if node.is_word:
                results.append(self.helper(j + 1))
            j += 1
        
        # skip char
        results.append(1 + self.helper(index + 1))

        result = min(results)
        self.cache[index]= result

        return result
