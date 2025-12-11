class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_t = Counter(t)
        count_s = Counter(s)
        ans = 0
        for k, v in count_s.items():
            have = count_t.get(k, 0)
            if have < v:
                ans += v - have
        return ans
        