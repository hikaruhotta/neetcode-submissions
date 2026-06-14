class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        bit_index = 1
        while n:
            bit_index_value = n & 1
            res = res | (bit_index_value << (32 - bit_index))
            n = n >> 1
            bit_index += 1
        return res