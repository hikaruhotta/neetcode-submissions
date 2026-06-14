class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {node: set() for node in range(numCourses)}
        in_degrees = {node: 0 for node in range(numCourses)}

        for first, second in prerequisites:
            edges[first].add(second)
            in_degrees[second] += 1
        
        level = set([node for node in in_degrees.keys() if in_degrees[node] == 0])

        order = []

        while level:
            next_level = set()
            order += list(level)

            for node in level:
                for adjacent in edges[node]:
                    in_degrees[adjacent] -= 1
                    if in_degrees[adjacent] == 0:
                        next_level.add(adjacent)
                del edges[node]
        
            level = next_level
        
        if len(edges) == 0:
            return order[::-1]
        else:
            return []
        

