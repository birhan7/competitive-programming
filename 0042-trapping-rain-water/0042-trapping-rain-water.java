class Solution {
    public int trap(int[] height) {
        int[] maxLeftHeight = new int[height.length];
        int[] maxRightHeight = new int[height.length];

        maxLeftHeight[0] = 0;
        maxRightHeight[height.length - 1] = 0;

        for(int i = 1; i < height.length; i++){
            maxLeftHeight[i] = Math.max(maxLeftHeight[i - 1], height[i - 1]);
        }

        for(int i = height.length - 2; i >= 0; i--){
            maxRightHeight[i] = Math.max(maxRightHeight[i + 1], height[i + 1]);
        }

        int ans = 0;
        for(int i = 0; i < height.length; i++){
            int trapped = Math.min(maxRightHeight[i], maxLeftHeight[i]) - height[i];
            if(trapped > 0){
                ans += trapped;
            }
        }
        return ans;
    }
}