class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        business = set(["electronics", "grocery", "pharmacy", "restaurant"])
        order = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        def check(idx):
            coupon = code[idx]
            return (businessLine[idx] in business) and isActive[idx] and all(c.isalnum() or c == "_" for c in coupon) and coupon
        
        ans = []
        for i in range(len(code)):
            if check(i):
                ans.append((businessLine[i], code[i]))
        ans.sort(key=lambda x: (order[x[0]], x[1]))
        res = [c for _,c in ans]
        return res
        

            
        
        