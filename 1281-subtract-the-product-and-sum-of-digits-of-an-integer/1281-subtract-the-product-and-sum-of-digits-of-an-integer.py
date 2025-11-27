class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ, product = 0, 1
        while n:
            rem = n % 10
            summ += rem
            product *= rem
            n = n // 10
        return product - summ
        