class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        
        carry = 0
        for i, digit in enumerate(reversed(digits)):
            if i == 0:
                digit += 1
            
            digit += carry
            carry = 0
            
            if digit > 9:
                carry = 1
                digit %= 10 
            
            res.append(digit)

        if carry == 1:
            res.append(1)

        return res[::-1]

