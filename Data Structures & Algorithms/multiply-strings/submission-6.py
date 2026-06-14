class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = self.zeroFill(num1, num2)
        
        num1 = num1[::-1]
        num2 = num2[::-1]

        results = []
        for i in range(len(num1)):
            res = ""
            for j in range(len(num2)):
                tmp = str(int(num1[i]) * int(num2[j])) + j * "0"
                res = self.sum(res, tmp)
            
            res += i * "0"
            results.append(res)
        
        final_res = ""
        for result in results:
            final_res = self.sum(final_res, result)

        print(final_res)

        return self.removeLeadingZeros(final_res)

    def zeroFill(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            zero_padding = (len(num1) - len(num2)) * "0"
            num2 = zero_padding + num2
        else:
            zero_padding = (len(num2) - len(num1)) * "0"
            num1 = zero_padding + num1
        return (num1, num2)

    def removeLeadingZeros(self, num: str) -> str:
        if len(num) == 0 or len(num) == 1:
            return num
        
        i = 0
        while i < len(num) and num[i] == '0':
            i += 1
        
        if i == len(num):
            return "0"
        
        return num[i:]

    def sum(self, num1: str, num2: str) -> str:
        num1, num2 = self.zeroFill(num1, num2)

        num1, num2 = num1[::-1], num2[::-1]

        res = ""
        
        carry = 0
        for i in range(len(num1)):
            dig1 = int(num1[i])
            dig2 = int(num2[i])
            add = dig1 + dig2 + carry
            carry = 0
            if add >= 10:
                carry = 1
        
            res += str(add % 10)

        if carry == 1:
            res += '1'
        
        return res[::-1]
            
            

        
