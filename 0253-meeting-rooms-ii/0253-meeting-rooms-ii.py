class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = []
        ends = []
        ans = 0
        for s, e in intervals:
            starts.append(s)
            ends.append(e)
        starts.sort()
        ends.sort()
       

        startIdx = 0
        curr = 0
        for e in ends:
            while startIdx < len(starts) and starts[startIdx]<e:
                curr+=1
                startIdx+=1
            ans = max(ans, curr)
            curr -= 1
        return ans
        cur =3