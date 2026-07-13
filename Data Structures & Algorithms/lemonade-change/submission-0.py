class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = [0, 0, 0] # 20, 10, 5
        money = [20, 10, 5]

        for bill in bills:
            if bill == 20:
                cash[0] += 1
            elif bill == 10:
                cash[1] += 1
            else:
                cash[2] += 1

            change = bill - 5
            i = 0
            while i < len(cash) and change > 0:
                if cash[i] > 0 and money[i] <= change:
                    change -= money[i]
                    cash[i] -= 1
                else:
                    i += 1
            if change > 0:
                return False
        
        return True

