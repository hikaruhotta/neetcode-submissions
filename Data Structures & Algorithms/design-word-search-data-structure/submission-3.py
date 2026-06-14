class TrieNode:

    def __init__(self):
        self.trie = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.addWordHelper(word, self.root)
    
    def addWordHelper(self, word: str, node: TrieNode) -> None:
        if len(word) == 0:
            node.is_word = True
            return

        if word[0] not in node.trie:
            node.trie[word[0]] = TrieNode()

        self.addWordHelper(word[1:], node.trie[word[0]])    

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.root)
    
    def searchHelper(self, word, node: TrieNode) -> bool:
        if len(word) == 0:
            return node.is_word
        
        if word[0] != '.':
            if word[0] not in node.trie:
                return False
            
            return self.searchHelper(word[1:], node.trie[word[0]])
        
        results = []
        for ch in node.trie:
            results.append(self.searchHelper(word[1:], node.trie[ch]))
        return any(results)
        
