class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def check(size):
            heater_index = 0
            index = 0
            while index < len(houses):
                if houses[index] < heaters[heater_index] - size or houses[index] > heaters[heater_index] + size:
                    heater_index += 1
                    if heater_index < len(heaters):
                        continue
                    else:
                        return False
                index += 1
            return True

        houses.sort()
        heaters.sort()
        low, high = 0, 10**9
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low