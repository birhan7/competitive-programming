class Solution:
    def canCross(self, stones: List[int]) -> bool:
        length = len(stones)
        dic = {}
        for i in range(length):
            dic[stones[i]] = i
        memo = {}
        def dfs(i, k):
            if i not in dic:
                return False
            if dic[i] == length - 1:
                return True
            if (i, k) not in memo:
                temp = False
                for j in [k - 1, k, k + 1]:
                    if j > 0:
                        temp = temp or dfs(i + j, j)
                        if temp:
                            break
                memo[(i, k)] = temp
            return memo[(i, k)]
        return dfs(dic[0], 0)
        