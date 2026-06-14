class PrefixTree:

    def __init__(self):
        self.trie = ({}, False)
        

    def insert(self, word: str) -> None:
        self.insertHelper(word, self.trie)

    def insertHelper(self, word, trie) -> None:
        if len(word) == 0:
            return

        tree, end = trie
        
        if word[0] not in tree:
            tree[word[0]] = ({}, False)

        if len(word) == 1:
            tree[word[0]] = (tree[word[0]][0], True)
        
        self.insertHelper(word[1:], tree[word[0]])


    def search(self, word: str) -> bool:
        result = self.searchHelper(word, self.trie)
        return result
    
    def searchHelper(self, word, trie) -> bool:
        tree, end = trie

        if len(word) == 0:
            return end
        
        if word[0] not in tree:
            return False
        
        return self.searchHelper(word[1:], tree[word[0]])

    def startsWith(self, prefix: str) -> bool:
        return self.startsWithHelper(prefix, self.trie)

    def startsWithHelper(self, prefix, trie) -> bool:
        if len(prefix) == 0:
            return True
        
        tree, end = trie
        if prefix[0] not in tree:
            return False
        
        return self.startsWithHelper(prefix[1:], tree[prefix[0]])



        
        