class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        business = {"electronics", "grocery", "pharmacy", "restaurant"}
        def is_valid(coupon):
            return (coupon[1].replace('_', 'a').isalnum() and (coupon[0] in business) and coupon[2])
        
        ans = sorted((filter(is_valid, zip(businessLine, code, isActive))))
        return [id for _, id ,_ in ans]
        
        

            
        
        