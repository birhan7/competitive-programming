class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        no_rooms = [0] * len(rooms)
        queue = deque([0]) 
        keys = set([0])
        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                for i in rooms[curr]:
                    if i not in keys:
                        keys.add(i)
                        queue.append(i)
                no_rooms[curr] = 1
        return sum(no_rooms) == len(rooms)