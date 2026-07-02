class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        people = sorted(people)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            
            result += 1
        
        return result


                