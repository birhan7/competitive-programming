class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix = [0] 
        n = len(nums)
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])

        count = 0
        for i in range(1, n):
            if (2 * prefix[i] - prefix[n]) % 2 == 0:
                count += 1
        return count
        