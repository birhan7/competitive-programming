class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations) - 1
        def check(size):
            low, high = 0, n
            while low <= high:
                mid = (low + high) // 2
                if citations[mid] < size:
                    low = mid + 1
                else:
                    high = mid - 1
            return (n - low)+1 >= size

        low, high = 0, max(citations)
        while low <= high:
            mid = (low + high)//2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
        