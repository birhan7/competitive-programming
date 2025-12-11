class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        for r in range(n):
            if s[r] == ']':
                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                k = int(stack.pop())
                base = 10
                while stack and stack[-1].isdigit():
                    k += (int(stack.pop()) * base)
                    base *= 10
                stack.append(temp * k)
            else:
                stack.append(s[r])
        ans = "".join(stack)
     
        return ans
        