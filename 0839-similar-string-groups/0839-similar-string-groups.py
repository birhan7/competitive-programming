class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind()
        for i in range(n):
            for j in range(n):
                if i != j:
                    if self.check(strs,i,j):
                        uf.union(strs[i],strs[j])
                        uf.find(strs[i])
                    uf.find(strs[j])
        count = Counter(uf.parent.values())
        return len(count)

    def check(self,strs,i,j):
        str1, str2 = strs[i], strs[j]
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
            if count > 2:
                return False
        return True
    


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = defaultdict(int)

    def find(self,ch):
        if ch not in self.parent:
            self.parent[ch] = ch
            self.size[ch] += 1
        if self.parent[ch] == ch:
            return ch
        self.parent[ch] = self.find(self.parent[ch])
        return self.parent[ch]

    def union(self,ch1, ch2):
        p1, p2 = self.find(ch1), self.find(ch2)
        s1, s2 = self.size[ch1], self.size[ch2]
        if p1 != p2:
            if s1 > s2:
                self.parent[p2] = p1
                self.size[p1] += self.size[p1]
            else:
                self.parent[p1] = p2
                self.size[p2] += self.size[p1]

    def connected(self,ch1, ch2):
        return self.find(ch1) == self.find(ch2)
        