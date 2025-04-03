class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        M, m = min(nums), max(nums)
        size = (m - M)+1
        buckets = [[] for _ in range(size)]
        if M > 0:
            for i in nums:
                buckets[i-1].append(i)
        else:
            for i in nums:
                buckets[i + abs(M)].append(i)
        ans = []
        buckets.sort(key= lambda bucket:len(bucket),reverse=True)
        for i in range(k):
            ans.append(buckets[i][0])
        return ans

        