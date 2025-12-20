class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        count = Counter(words)
        for key in count:
            heap.append((count[key], key))
            if len(heap) > k:
                heap.sort(key= lambda item: (-item[0], item[1]))
                heap.pop()
        heap.sort(key= lambda item: (-item[0], item[1]))
        return list(map(lambda item: item[1], heap))
       

        
        