class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # a -> b means a is trusted by b
        # a: [] means all the people who trust a
        graph_inverse = {i: [] for i in range(1, n + 1)}
        indegree_inverse = {i: 0 for i in range(1, n + 1)}
        for trust_i in trust:
            a, b = trust_i[0], trust_i[1]
            graph_inverse[b].append(a)
            indegree_inverse[a] += 1
        
        candidates = set()
        # town judge has inverse indegree of 0
        for key, val in indegree_inverse.items():
            if val == 0:
                candidates.add(key)

        # two judge is trusted by everyone else
        for candidate in candidates.copy():
            if len(graph_inverse[candidate]) < n - 1:
                candidates.remove(candidate)

        # there is only one such individual
        if len(list(candidates)) == 1:
            return list(candidates)[0]
        
        return -1
        
        
        


