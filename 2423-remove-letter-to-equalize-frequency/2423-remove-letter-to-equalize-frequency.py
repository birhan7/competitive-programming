class Solution:
    def equalFrequency(self, word: str) -> bool:
        word_dict = Counter(word)
        key_set = list(word_dict.keys())

        for key in key_set:
            word_dict[key]-=1
            if word_dict[key]==0:
                word_dict.pop(key)

            if len(set(word_dict.values()))==1:
                return True
            word_dict[key]+=1

        return False
        


        