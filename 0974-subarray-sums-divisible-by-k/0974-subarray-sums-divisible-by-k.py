class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = defaultdict(int)
        prefix[0] = 1
        curr, count = 0, 0
        for i in range(n):
            curr += nums[i]
            curr %= k
            count += prefix[curr]
            prefix[curr] += 1
        return count
        