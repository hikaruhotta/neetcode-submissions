class UnionFind:

    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n) -> int:
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = set()
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emails.add(email)
                email_to_name[email] = name
        
        emails_list = sorted(emails)
        emails_dict = {email: (i, email_to_name[email]) for i, email in enumerate(emails_list)}

        union_find = UnionFind(len(emails_list))

        for account in accounts:
            email_list = account[1:]
            for i in range(len(email_list) - 1):
                e1 = emails_dict[email_list[i]][0]
                e2 = emails_dict[email_list[i + 1]][0]
                union_find.union(e1, e2)
        
        groups = {}
        for i in range(len(emails_list)):
            par = union_find.find(i)
            if par not in groups:
                groups[par] = []
            groups[par].append(i)
        
        result = []

        for key, email_indicies in groups.items():
            email_addrs = []
            for index in email_indicies:
                email_addrs.append(emails_list[index])
            name = emails_dict[email_addrs[0]][1]
            result.append([name] + email_addrs)

        return result

