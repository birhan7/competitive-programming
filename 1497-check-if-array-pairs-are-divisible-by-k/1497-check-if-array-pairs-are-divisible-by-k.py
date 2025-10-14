class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        bucket = [0] * k
        for n in arr:
            bucket[n % k] += 1
        if k % 2 == 0 and bucket[k // 2]%2:
            return False
        for i in range(k):
            if bucket[i] != bucket[(-i) % k]:
                return False
        return True

        