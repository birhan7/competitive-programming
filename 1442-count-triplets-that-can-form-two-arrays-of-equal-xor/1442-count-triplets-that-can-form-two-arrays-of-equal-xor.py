class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefixXOR = [arr[0]]
        n = len(arr)
        for i in range(1,n):
            prefixXOR.append(prefixXOR[-1] ^ arr[i])
        count = 0
        for i in range(n):
            for k in range(n):
                if k > i:
                    if i > 0 and prefixXOR[k] - prefixXOR[i-1] == 0:
                        count += k - i
                    elif i == 0 and prefixXOR[k] == 0:
                        count += k
        return count
            
            
        