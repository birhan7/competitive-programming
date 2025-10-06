class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        initial = 0
        for i in operations:
            if i == "--X" or i == "X--":
                initial -= 1
            else:
                initial += 1
        return initial
        