class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        prefix = [0] * n
        for i in range(n - 1, -1, -1):
            prev = i + k
            if prev < n:
                prefix[i] = prefix[prev] 
            prefix[i] += energy[i]
        return max(prefix)

        