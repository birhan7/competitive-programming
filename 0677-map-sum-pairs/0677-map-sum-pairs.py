class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.total = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None: 
        curr = self.root
        for ch in key:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.total = val
        curr.is_end = True
        
    def sum(self, prefix: str) -> int:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return self.count(curr)

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False, 0
            curr = curr.children[ch]
        return curr.is_end, curr.total
    
    def count(self, curr):
        total = 0
        if curr.is_end:
            total += curr.total
        if curr:
            for ch in curr.children:
                total += self.count(curr.children[ch])
        return total

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)