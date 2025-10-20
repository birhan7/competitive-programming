 

class WordFilter:

    def __init__(self, words: List[str]):
        self.comb = {}
        for index in range(len(words)):
            word = words[index]
            n = len(word)
            for i in range(1, n + 1):
                prefix = word[:i]
                for j in range(n):
                    suffix = word[j:]
                    self.comb[prefix + '#' + suffix] = index

    def f(self, pref: str, suff: str) -> int:
        return self.comb.get(pref + '#' + suff, -1)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)