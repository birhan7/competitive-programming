class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
    
    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def dp(l, r, path):
            if r == len(s) - 1:
                word = s[l: r + 1]
                if word in wordDict:
                    path += " " + word
                    path = path.strip()
                    ans.append(path)
                return
            word = s[l: r + 1]
            if word in wordDict:
                dp(r + 1, r + 1, path + " " + word)
            dp(l, r + 1, path)
        dp(0, 0, "")
        return ans
                
        
        