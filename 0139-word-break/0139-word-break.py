class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        n = len(s)
        dic = set(wordDict)
        def dp(l, r):
            if r == n and s[l:r + 1] in dic:
                return True
            if r == n:
                return False
            if (l, r) not in memo:
                include = False
                if s[l:r+1] in dic:
                    include = dp(r + 1, r + 1)
                exclude = dp(l,r + 1)
                memo[(l, r)] = include or exclude
            return memo[(l, r)]
        return dp(0,0)
        