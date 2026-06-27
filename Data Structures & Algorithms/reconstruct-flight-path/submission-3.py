from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for i, ticket in enumerate(tickets):
            from_i, to_i = ticket[0], ticket[1]
            if from_i not in graph:
                graph[from_i] = []
            graph[from_i].append((to_i, i)) # destination, ticket_index
        
        for key, val in graph.items():
            graph[key] = sorted(graph[key], key=lambda x: x[0])
        
        self.result = []
        self.graph, self.tickets = graph, tickets
        self.helper("JFK", ["JFK"], [True for i in range(len(tickets))])
        return self.result

    def helper(self, from_i: str, path: List[str], available_tickets: List[bool]) -> None:
        if self.result:
            return

        if len(path) == len(self.tickets) + 1:
            self.result = path.copy()
            return

        if from_i in self.graph:
            for to_i, ticket_index in self.graph[from_i]:
                if available_tickets[ticket_index]:
                    path.append(to_i)
                    available_tickets[ticket_index] = False
                    self.helper(to_i, path, available_tickets)
                    available_tickets[ticket_index] = True
                    path.pop()