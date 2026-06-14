class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(delta) < 0:
            return -1

        starting_index = 0
        running_sum = 0
        for i in range(len(delta)):
            running_sum += delta[i]

            if running_sum < 0:
                running_sum = 0
                starting_index = i + 1
        
        return starting_index


