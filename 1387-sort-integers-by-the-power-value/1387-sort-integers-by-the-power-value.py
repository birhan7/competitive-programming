class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power_of_num(num):
            count = 0
            while num != 1:
                if num % 2 == 0:
                    num /= 2
                else:
                    num = 3 * num + 1
                count += 1
            return count
        nums = []
        for num in range(lo, hi + 1):
            nums.append((power_of_num(num), num))
        nums.sort()
        return nums[k - 1][1]
        