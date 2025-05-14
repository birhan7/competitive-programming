class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXOR = [arr[0]]
        n = len(arr)
        for i in range(1,n):
            prefixXOR.append(prefixXOR[-1]^arr[i])
        
        ans = []
        m = len(queries)
        for i in range(m):
            l, r = queries[i]
            if l == 0:
                ans.append(prefixXOR[r])
            else:
                ans.append(prefixXOR[r]^prefixXOR[l-1])
        return ans
        