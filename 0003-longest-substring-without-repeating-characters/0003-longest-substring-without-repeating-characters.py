class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        chars = defaultdict(int)
        ans = 0
        for r in range(n):
            ch = s[r]
            chars[ch] += 1
            if chars[ch] <= 1:
                ans = max(ans, r - l + 1)
            while chars[ch] > 1:
                chars[s[l]] -= 1
                l += 1
        return ans



        