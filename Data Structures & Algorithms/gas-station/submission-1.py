class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(delta) < 0:
            return -1

        print(delta)

        starting_index = 0
        running_sum = 0
        while True:
            for i in range(len(delta)):
                running_sum += delta[(starting_index + i) % len(delta)]
                print(running_sum)
                if running_sum < 0:
                    starting_index = (starting_index + i + 1) % len(delta)
                    running_sum = 0
                    break
            if i == len(delta) - 1:
                return starting_index

        return -1

