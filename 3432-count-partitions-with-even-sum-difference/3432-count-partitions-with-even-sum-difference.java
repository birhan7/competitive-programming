class Solution {
    public int countPartitions(int[] nums) {
        int answer = 0; 
        int left =0;
        int total = 0;
        for (int k = 0; k < nums.length; k ++){
            total += nums[k];
        }
        if (total % 2 != 0){
            return answer;
        }
        for (int i =0; i < nums.length - 1 ; i++ ){
             left += nums[i];
             int right = total - left; 
            
        int difference = right - left ;
        if (difference % 2 == 0){
            answer += 1;
        }
        }
        return answer;
    }
}