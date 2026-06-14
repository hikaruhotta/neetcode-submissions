class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if sum(stones) % 2 == 0:
            target = sum(stones) // 2
        else:
            target = sum(stones) // 2 + 1
        
        dp = [False] * (target + 1)

        index = 0
        dp[0] = True
        for t in range(1, target + 1):
            if t == stones[index]:
                dp[t] = True
        
        for index in range(1, len(stones)):
            next_dp = [False] * (target + 1)

            for t in range(target + 1):
                skip = dp[t]

                include = False
                if stones[index] <= t:
                    include = dp[t - stones[index]]
                
                next_dp[t] = skip or include
            
            dp = next_dp
        
        max_t = 0
        for t in range(len(dp)):
            if dp[t]:
                max_t = t
        
        complement = sum(stones) - max_t

        return abs(complement - max_t)
                

            