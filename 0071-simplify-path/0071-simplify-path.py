class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        left = 0
        right = 1
        length = len(path)
        while right < length:
            if path[right] == "/":
                if  left + 1 == right:
                    left = right
                elif path[left+1:right] == "..":
                    if stack:
                        stack.pop()
                    left = right
                elif path[left+1:right] == ".":
                    left = right
                else:
                    stack.append(path[left+1:right])
                left = right
            elif right == length - 1:
                lefted = path[left+1:]
                if lefted == "..":
                    if stack:
                        stack.pop()
                elif lefted != ".":
                    stack.append(lefted)
                break
            right += 1

        return "/" + "/".join(stack)
        
        