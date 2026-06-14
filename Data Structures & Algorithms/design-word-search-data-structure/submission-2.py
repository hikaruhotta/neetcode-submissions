class WordDictionary:

    def __init__(self):
        self.trie = ({}, False)
        
    def addWord(self, word: str) -> None:
        trie_level = self.trie
        for i, ch in enumerate(word):
            trie, word_end = trie_level
            if ch not in trie:
               trie[ch] = ({}, False)
            if i == len(word) - 1:
                trie[ch] = (trie[ch][0], True)
            trie_level = trie[ch]

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.trie)

    def searchHelper(self, word, trie_level):
        trie, word_end = trie_level
        if len(word) == 0:
            return word_end
        
        if word[0] == '.':
            for ch in trie:
                if self.searchHelper(word[1:], trie[ch]):
                    return True
        else:
            if word[0] in trie:
                if self.searchHelper(word[1:], trie[word[0]]):
                    return True
        
        return False




        
