class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_word = strs[0]
        smallest_length = len(smallest_word)
        for i in range(len(strs)):
            word = strs[i]
            length = len(word)
            if length < smallest_length:
                smallest_word = word
                smallest_length = length
        ans = ''
        flag = True
        for i in range(smallest_length):
            for j in range(len(strs)):
                word = strs[j]
                if word[i] != smallest_word[i]:
                    flag = False
                    break
            if not flag:
                break
            else:
                ans += smallest_word[i]
        
        return ans
                    

        