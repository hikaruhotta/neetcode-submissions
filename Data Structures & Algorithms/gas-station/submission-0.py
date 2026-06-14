class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(delta) < 0:
            return -1
        
        for starting_index in range(len(delta)):
            running_sum = delta[starting_index]
            index = (starting_index + 1) % len(delta)
            while running_sum >= 0 and index != starting_index:
                running_sum += delta[index]
                index = (index + 1) % len(delta)
            if index == starting_index:
                return starting_index
            else:
                continue

        return -1

