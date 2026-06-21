from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cnt = Counter(hand)
        while cnt:
            min_val = min(list(cnt.keys()))
            for i in range(groupSize):
                if min_val + i not in cnt:
                    return False
                else:
                    cnt[min_val + i] -= 1
                    if cnt[min_val + i] == 0:
                        del cnt[min_val + i]
        return True



