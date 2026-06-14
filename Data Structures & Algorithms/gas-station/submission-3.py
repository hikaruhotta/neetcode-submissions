class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        deltas = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(deltas) < 0:
            return -1
        
        start_index = 0
        while start_index < len(deltas):
            if deltas[start_index] < 0:
                start_index += 1
                continue
            
            tank = 0
            index = start_index
            num_steps = 0
            while tank >= 0 and num_steps < len(deltas):
                tank += deltas[index]
                index += 1
                index = index % len(deltas)
                num_steps += 1
            
            if num_steps == len(deltas) and tank >= 0:
                return start_index
            
            start_index = index

        return -1



            
            
            

        




