class TrieNode:

    def __init__(self):
        self.trie = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.trieRoot = TrieNode()
        self.trieRoot.is_word = True

    def insert(self, word: str) -> None:
        self.insertHelper(word, self.trieRoot)
    
    def insertHelper(self, word: str, trieNode: TrieNode) -> None:
        if len(word) == 0:
            trieNode.is_word = True
            return
        
        if word[0] not in trieNode.trie:
            trieNode.trie[word[0]] = TrieNode()
        
        self.insertHelper(word[1:], trieNode.trie[word[0]])


    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.trieRoot, False)

    def startsWith(self, prefix: str) -> bool:
        return self.searchHelper(prefix, self.trieRoot, True)

    def searchHelper(self, word: str, trieNode: TrieNode, isPrefix: bool) -> bool:
        if len(word) == 0:

            return isPrefix or trieNode.is_word
        
        if word[0] not in trieNode.trie:
            return False
        
        return self.searchHelper(word[1:], trieNode.trie[word[0]], isPrefix)
        
        
        