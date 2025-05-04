class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = ""
        num = ""
        char = ""
        for i in range(len(s)):
            if s[i] == "[":
                if num:
                    stack.append(num)
                    num = ""
                stack.append(0)
            elif s[i] == "]":
                while stack[-1] != 0:
                    ch = stack.pop()
                    if ch.isdigit():
                        char = char * int(ch)
                    else:
                        char = ch + char
                stack.pop()
                if stack:
                    ch = stack.pop()
                    if ch.isdigit():
                        char = char * int(ch)
                    else:
                        char = ch + char
                stack.append(char)
                char = ""
            else:
                if s[i].isdigit():
                    if char:
                        stack.append(char)
                        char = ""
                    num += s[i]
                else:
                    char += s[i]
            
        if char:
            stack.append(char)
        return "".join(stack)
        


        