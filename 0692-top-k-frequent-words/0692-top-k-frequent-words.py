class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        count_list = list(count.items())
        count_list.sort(key= lambda item: (-item[1], item[0]))
        ans = [item for item, _ in count_list]
        return ans[:k]
        
        