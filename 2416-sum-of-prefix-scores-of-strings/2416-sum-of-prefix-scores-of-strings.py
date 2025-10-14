class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
                current.children[ch].val = 1
            else:
                current.children[ch].val += 1
            current = current.children[ch]
        current.is_end = True
        
    def count(self, word):
        curr = self.root
        ans = 0
        for ch in word:
            curr = curr.children[ch]
            ans += curr.val
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = WordDictionary()
        for word in words:
            trie.addWord(word)
        ans = []
        for word in words:
            ans.append(trie.count(word))
        return ans
        