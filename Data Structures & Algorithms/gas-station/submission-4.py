class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        starting_index, i = 0, 0
        tank = 0
        while True:
            tank += gas[i]
            tank -= cost[i]
            i += 1
            i %= len(gas)
            if tank < 0:
                starting_index = i
                tank = 0
            elif i == starting_index:
                break
        
        return starting_index
        