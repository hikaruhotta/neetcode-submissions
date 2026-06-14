from collections import OrderedDict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for num in hand:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        count = OrderedDict(sorted(count.items(), key=lambda x: (x[0], -x[1])))

        for _ in range(len(hand) // groupSize):
            group = []
            for _ in range(groupSize):
                if len(group) == 0:
                    num = list(count.items())[0][0]
                    count[num] -= 1
                    if count[num] == 0:
                        del count[num]
                    group.append(num)
                else:
                    prev_num = group[-1]
                    if prev_num + 1 not in count:
                        return False
                    count[prev_num + 1] -= 1
                    if count[prev_num + 1] == 0:
                        del count[prev_num + 1]
                    group.append(prev_num + 1)
        
        return True

                



        
