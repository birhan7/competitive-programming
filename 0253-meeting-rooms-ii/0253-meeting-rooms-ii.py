class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        slot = []
        ans = 1
        for interval in intervals:
            if slot:
                end, dur = heapq.heappop(slot)
                if end > interval[0]:
                    heapq.heappush(slot, (end, dur))
            heapq.heappush(slot, (interval[1], interval[1] - interval[0]))
            ans = max(ans, len(slot))
        return ans