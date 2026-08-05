class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int result = 0;
        int l = 0, r = 0;
        while(r < n - 1){
            int farthest = 0;
            for(int j = l; j <= r; j ++){
                farthest = Math.max(nums[j] + j, farthest);
            }
            l = r + 1;
            r = farthest;
            result += 1;
        }
        return result;
    }
}