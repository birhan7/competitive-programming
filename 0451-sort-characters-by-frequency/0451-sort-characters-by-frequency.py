class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_ch = list(count.keys())
        sorted_ch.sort(key=lambda x: count[x], reverse=True)
        ans = ""
        for ch in sorted_ch:
            ans += ch * count[ch]
        return ans
        
        