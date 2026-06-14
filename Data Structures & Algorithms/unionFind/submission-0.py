class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

        self.num_components = n
        

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        p_x, p_y = self.find(x), self.find(y)
        r_x, r_y = self.rank[p_x], self.rank[p_y]

        if p_x == p_y:
            return False
        
        if r_x > r_y:
            self.par[p_y] = p_x
        elif r_x < r_y:
            self.par[p_x] = p_y
        else:
            self.par[p_x] = p_y
            self.rank[p_y] += 1

        self.num_components -= 1
        return True
        

    def getNumComponents(self) -> int:
        return self.num_components


