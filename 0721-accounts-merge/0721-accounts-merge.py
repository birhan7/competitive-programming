class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind()
        ref = defaultdict(str)

        for i in range(n):
            m = len(accounts[i])
            parent = accounts[i][1]
            uf.insert(parent)
            for j in range(2,m):
                uf.insert(accounts[i][j])
                uf.union(parent,accounts[i][j])
            ref[uf.find(parent)] = accounts[i][0]

        ans = defaultdict(list)
        for key, val in uf.parent.items():
            ans[uf.find(val)].append(key)

        res = []
        for key,val in ans.items():
            val.sort()
            temp = [ref[key],*val]
            res.append(temp)

        res.sort()
        return res


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def insert(self,email):
        if email not in self.parent:
            self.parent[email] = email
        return email

    def find(self,email):
        if self.parent[email] == email:
            return email
        self.parent[email] = self.find(self.parent[email])
        return self.parent[email]

    def union(self,email_one, email_two):
        p1, p2 = self.find(email_one), self.find(email_two)
        self.parent[p2] = p1

    def connected(self,email_one, email_two):
        return self.find(email_one) == self.find(email_two)
        