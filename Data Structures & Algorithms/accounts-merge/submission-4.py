from collections import deque

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        for i, account in enumerate(accounts):
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email not in graph:
                    graph[email] = []
                graph[email].append(i)

        print(graph)

        merge_graph = {i: set() for i in range(len(accounts))}
        for key, values in graph.items():
            if len(values) > 0:
                for i in values:
                    for j in values:
                        if i != j:
                            merge_graph[i].add(j)

        print(merge_graph)
        
        visited = set()
        groups = []
        for key in merge_graph:
            if key not in visited:
                groups.append(self.helper(key, merge_graph, visited))

        print(groups)    

        result = []
        for group in groups:
            emails = set()
            for i in group:
                for email in accounts[i][1:]:
                    emails.add(email)
            emails = sorted(list(emails))
            result.append([accounts[group[0]][0]] + emails)

        return result

    def helper(self, account: int, graph: Dict, visited: set()) -> List[int]:
        result = []
        queue = deque([account])
        visited.add(account)
        while queue:
            acct = queue.popleft()
            result.append(acct)

            for node in graph[acct]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        return result


        

        