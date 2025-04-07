class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(path,no_open,no_closed):
            if (no_open + no_closed) == 2 * n:
                ans.append("".join(path))
                return
            elif no_open == no_closed:
                path.append("(")
                backtrack(path,no_open + 1, no_closed)
                path.pop()
            elif no_open > no_closed and no_open < n:
                path.append("(")
                backtrack(path,no_open + 1, no_closed)
                path.pop()
                path.append(")")
                backtrack(path,no_open, no_closed + 1)
                path.pop()
            else:
                path.append(")")
                backtrack(path, no_open, no_closed + 1)
                path.pop()
        backtrack([],0,0)
        return ans
        