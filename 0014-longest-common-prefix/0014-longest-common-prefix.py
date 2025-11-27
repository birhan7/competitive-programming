class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for i in range(len(word)):
            ch = word[i]
            for w in strs:
                if i == len(w) or ch != w[i]:
                    return word[:i]
        return word
                    

        