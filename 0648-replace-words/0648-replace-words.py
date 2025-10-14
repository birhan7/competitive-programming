class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end = True
        
    def search(self, word):
        curr = self.root
        length = len(word)
        for i in range(length):
            if word[i] in curr.children and not curr.is_end:
                curr = curr.children[word[i]]
            else:
                break
        return i if curr.is_end else 0

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = WordDictionary()
        for word in dictionary:
            trie.addWord(word)
        ans = ""
        temp = sentence.split()
        for word in temp:
            index = trie.search(word)
            if index == 0:
                ans += word + " "
            else:
                ans += word[:index] + " "
        return ans.rstrip()
        