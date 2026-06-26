class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 0
        for i, digit in enumerate(digits):
            total = digit + carry
            if i == 0:
                total += 1
            carry = 0
            if total > 9:
                carry = 1
            digits[i] = total % 10
        if carry == 1:
            digits.append(1)
        return digits[::-1]