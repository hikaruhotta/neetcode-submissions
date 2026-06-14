class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_triplets = []
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            valid_triplets.append(triplet)
        
        found = [False, False, False]
        for triplet in valid_triplets:
            for i in range(3):
                if triplet[i] == target[i]:
                    found[i] = True
        return all(found)