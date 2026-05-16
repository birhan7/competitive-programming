class Solution {
    public void sortColors(int[] nums) {
        int left = 0, right = nums.length - 1, i = 0;
        while(i <= right){
            int temp = nums[i];
            if(nums[i] == 0){
                nums[i] = nums[left];
                nums[left] = temp;
                left++;
                i++;
            }else if(nums[i] == 2){
                nums[i] = nums[right];
                nums[right] = temp;
                right--;
            }else{
                i++;
            }
        }
        
    }
}