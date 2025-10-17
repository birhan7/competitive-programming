class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        memo = {}
        def dfs(i):
            if i >= length:
                return 0
            if i not in memo:
                p, bp = questions[i]
                include = p + dfs(i + bp + 1)
                exclude = dfs(i + 1)
                memo[i]  = max(include, exclude)
            return memo[i]
        return dfs(0)
        