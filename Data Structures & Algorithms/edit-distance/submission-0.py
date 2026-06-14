class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        self.cache = {}
        return self.dfs(0, 0)
    
    def dfs(self, word1_index: int, word2_index: int) -> int:
        # AT LEAST ONE WORD IS AT END
        if word1_index == len(self.word1) and word2_index == len(self.word2):
            return 0
        elif word1_index != len(self.word1) and word2_index == len(self.word2):
            # number of delete operations required to match
            return len(self.word1) - word1_index
        elif word1_index == len(self.word1) and word2_index != len(self.word2):
            # number of insert operations required to match
            return len(self.word2) - word2_index

        if (word1_index, word2_index) in self.cache:
            return self.cache[(word1_index, word2_index)]

        # Matching - no operation required
        if self.word1[word1_index] == self.word2[word2_index]:
            result = self.dfs(word1_index + 1, word2_index + 1)
            self.cache[(word1_index, word2_index)] = result
            return result

        candidates = []

        # insert
        candidates.append(1 + self.dfs(word1_index, word2_index + 1))

        # delete
        candidates.append(1 + self.dfs(word1_index + 1, word2_index))

        #replace
        candidates.append(1 + self.dfs(word1_index + 1, word2_index + 1))

        result = min(candidates)

        self.cache[(word1_index, word2_index)] = result

        return result
