class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {"]": "[", "}": "{", ")": "("}
        stack = []
        for ch in s:
            if ch not in parenthesis.keys():
                stack.append(ch)
            elif not stack or stack[-1] != parenthesis[ch]:
                return False
            else:
                stack.pop()
        return not stack

        