class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        ans = []
        def backtrack(i, path):
            if i >= len(digits):
                return ans.append(path)
            num = int(digits[i])
            for ch in digit_map[num]:
                path += ch
                backtrack(i + 1, path)
                path = path[:len(path) - 1]
        backtrack(0, "")
        return ans

        