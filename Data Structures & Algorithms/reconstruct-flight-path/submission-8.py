from collections import Counter

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for ticket in tickets:
            from_i, to_i = ticket[0], ticket[1]
            if from_i not in graph:
                graph[from_i] = []
            graph[from_i].append(to_i)
        
        for node in graph:
            graph[node] = sorted(graph[node])
        
        self.graph = graph
        self.tickets = tickets
        remaining_tickets = Counter([(ticket[0], ticket[1]) for ticket in tickets])
        self.result = []
        self.helper(['JFK'], remaining_tickets)
        return self.result
        
    def helper(self, path: List[str], remaining_tickets: Counter) -> None:
        if len(self.result) > 0:
            return

        if len(path) == len(self.tickets) + 1:
            self.result = path.copy()
            return

        if path[-1] in self.graph:
            for neighbor in self.graph[path[-1]]:
                if (path[-1], neighbor) in remaining_tickets and remaining_tickets[(path[-1], neighbor)] > 0:
                    remaining_tickets[(path[-1], neighbor)] -= 1
                    path.append(neighbor)
                    self.helper(path, remaining_tickets)
                    path.pop()
                    remaining_tickets[(path[-1], neighbor)] += 1
