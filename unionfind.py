class unionfind:
    sz = 0
    par = []
    def __init__(self, n):
        self.sz = n
        for i in range(n):
            self.par.append(-1)

    def find(self, a):
        if self.par[a]<0: return a
        self.par[a] = self.find(self.par[a])
        return self.par[a]
    
    def size(self, a):
        a = self.find(a)
        return -self.par[a]
    
    def same(self, a,b):
        return self.find(a) == self.find(b)

    def unite(self, a,b):
        a = self.find(a)
        b = self.find(b)
        if self.same(a,b): return False
        if self.size(a) < self.size(b):
            a,b=b,a
        self.par[a] += self.par[b]
        self.par[b] = a
        return True



"""
verify
size n, query q

query
0 a b -> unite a and b
1 a b -> if united a and b -> 1, else -> 0
"""
if __name__ == "__main__"
    n,q = map(int,input().split())
    UF = unionfind(n)
    for _ in range(q):
        c,a,b = map(int,input().split())
        a,b = a-1,b-1
        if c == 0:
            UF.unite(a,b)
        else:
            if UF.same(a,b):
                print(1)
            else : print(0)