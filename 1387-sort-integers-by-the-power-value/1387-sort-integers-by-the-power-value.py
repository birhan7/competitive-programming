class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power_of_num(x):
            num = x
            count = 0
            while True:
                if num in memo:
                    memo[x] = count + memo[num]
                    break
                elif num % 2 == 0:
                    num /= 2
                else:
                    num = 3 * num + 1
                count += 1
            return memo[x]
        memo = {1: 0}
        nums = []
        for num in range(lo, hi + 1):
            nums.append((power_of_num(num), num))
        nums.sort()
        return nums[k - 1][1]
        