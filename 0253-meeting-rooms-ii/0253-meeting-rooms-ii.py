class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        slot = []
        for interval in intervals:
            if slot and slot[0] <= interval[0]:
                heapq.heappop(slot)
            heapq.heappush(slot, interval[1])
        return len(slot)