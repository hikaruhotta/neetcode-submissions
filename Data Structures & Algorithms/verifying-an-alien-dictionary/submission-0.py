class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {ch: i + 1 for i, ch in enumerate(order)}
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))
        vec_words = [[0] * max_len for word in words]
        for i, word in enumerate(words):
            for j, ch in enumerate(word):
                vec_words[i][j] = order[ch]

        print(vec_words)

        for i in range(len(vec_words) - 1):
            for j in range(len(vec_words[i])):
                if vec_words[i][j] < vec_words[i + 1][j]:
                    break
                
                if vec_words[i][j] > vec_words[i + 1][j]:
                    return False
        
        return True