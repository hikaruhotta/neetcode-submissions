class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [1, 1, 1]
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                result = [max(result[0], triplet[0]), max(result[1], triplet[1]), max(result[2], triplet[2])]
        return all([result[i] == target[i] for i in range(3)])