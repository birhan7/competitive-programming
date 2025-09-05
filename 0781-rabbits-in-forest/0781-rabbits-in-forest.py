class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for k, v in count.items():
            if k == 0:
                ans += v
            else:
                ans += math.ceil(v / (k + 1)) * (k + 1)
        return ans

        