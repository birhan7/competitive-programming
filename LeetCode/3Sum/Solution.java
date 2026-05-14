1class Solution {
2    public List<List<Integer>> threeSum(int[] nums) {
3        Arrays.sort(nums);
4        List<List<Integer>> ans = new ArrayList<>();
5        for (int i = 0; i < nums.length - 2; i++){
6            if (i > 0 && nums[i] == nums[i - 1]){
7                continue;
8            }
9            int left = i + 1, right = nums.length - 1;
10            while (left < right){
11                int sum = nums[i] + nums[left] + nums[right];
12                if (sum > 0){
13                    right --;
14                } else if (sum < 0) {
15                    left ++;
16                } else {
17                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));
18                    while (left < right && nums[left] == nums[left + 1]){
19                        left ++;
20                    }
21                    while (right > left && nums[right] == nums[left]){
22                        right --;
23                    }
24                    left ++;
25                    right --;
26                }
27            }
28        }
29        return ans;
30    }
31}