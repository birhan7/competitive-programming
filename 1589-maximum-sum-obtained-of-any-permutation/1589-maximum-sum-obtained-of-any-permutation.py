class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        single_index = defaultdict(int)
        prefix = [0] * (n + 1)
        for l, r in requests:
            if l == r:
                single_index[l] += 1
            else:
                prefix[l] += 1
                prefix[r + 1] += -1
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        for k, v in single_index.items():
            prefix[k] += v
        prefix.sort(reverse=True)
        nums.sort(reverse=True)
        ans = 0
        for i in range(n):
            ans += (nums[i] * prefix[i]) % (10**9 + 7)
        return ans % (10**9 + 7)



        