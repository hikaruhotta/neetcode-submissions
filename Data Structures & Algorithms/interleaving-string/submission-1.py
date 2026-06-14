class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False

        self.s1, self.s2, self.s3 = s1, s2, s3
        self.cache = {}
        return self.dfs(0, 0, True) or self.dfs(0, 0, False)

    def dfs(self, s1_index: int, s2_index: int, is_s1_turn: bool) -> bool:
        if s1_index == len(self.s1) and s2_index == len(self.s2):
            return True

        if (s1_index, s2_index, is_s1_turn) in self.cache:
            return self.cache[(s1_index, s2_index, is_s1_turn)]
        
        s3_index = s1_index + s2_index

        if is_s1_turn:
            s1_sub_str = ""
            s3_sub_str = ""
            for sub_str_len in range(len(self.s1) - s1_index):
                s1_sub_str += self.s1[s1_index + sub_str_len]
                s3_sub_str += self.s3[s3_index + sub_str_len]

                if s1_sub_str != s3_sub_str:
                    break
                
                if self.dfs(s1_index + sub_str_len + 1, s2_index, not is_s1_turn):
                    self.cache[(s1_index, s2_index, is_s1_turn)] = True
                    return True
        else:
            s2_sub_str = ""
            s3_sub_str = ""
            for sub_str_len in range(len(self.s2) - s2_index):
                s2_sub_str += self.s2[s2_index + sub_str_len]
                s3_sub_str += self.s3[s3_index + sub_str_len]

                if s2_sub_str != s3_sub_str:
                    break
                
                if self.dfs(s1_index, s2_index + sub_str_len + 1, not is_s1_turn):
                    self.cache[(s1_index, s2_index, is_s1_turn)] = True
                    return True
        
        self.cache[(s1_index, s2_index, is_s1_turn)] = False
        return False
            




        
