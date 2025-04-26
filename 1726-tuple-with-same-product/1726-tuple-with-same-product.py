class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_dict = {}
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                product_dict[nums[i] *nums[j]] = product_dict.get(nums[i] *nums[j],0) + 1
        num_tuples = 0
        for i in product_dict:
            if product_dict[i] >= 2:
                n = product_dict[i]
                num_tuples += (n * ( n - 1) // 2) * pow(2,3)
        return num_tuples

        



        