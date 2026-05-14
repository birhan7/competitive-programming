1class Solution {
2    public List<List<Integer>> threeSum(int[] nums) {
3        Arrays.sort(nums);
4        Set<List<Integer>> ans = new HashSet<>();
5        for (int l = 0; l < nums.length - 2; l++){
6            int m = l + 1, r = nums.length - 1;
7            while (m < r){
8                int sum = nums[l] + nums[m] + nums[r];
9                if (sum > 0){
10                    r --;
11                } else {
12                    if (sum == 0){
13                        ans.add(Arrays.asList(nums[l], nums[m], nums[r]));
14                    }
15                    m ++;
16                }
17            }
18        }
19        return new ArrayList<>(ans);
20    }
21}