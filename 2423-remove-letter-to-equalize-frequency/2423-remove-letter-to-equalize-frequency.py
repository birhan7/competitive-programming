class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(Counter(word).values())
        if len(count) == 1 and ((1 in count.keys()) or (1 in count.values())):
            return True
        elif len(count) == 2:
            if count.get(1, 0) == 1:
                return True
            elif count[max(count.keys())] == 1 and max(count.keys()) - min(count.keys()) == 1:
                return True
        return False

        
        


        