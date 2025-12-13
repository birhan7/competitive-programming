class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        business = ["electronics", "grocery", "pharmacy", "restaurant"]
        def check(idx):
            coupon = code[idx]
            return (businessLine[idx] in business) and isActive[idx] and all(c.isalnum() or c == "_" for c in coupon) and coupon
        
        temp = defaultdict(list)
        for i in range(len(code)):
            if check(i):
                temp[businessLine[i]].append(code[i])
        print(temp)
        ans = []
        for k in business:
            if temp[k]:
                temp[k].sort()
                ans.extend(temp[k])
        return ans
        

            
        
        