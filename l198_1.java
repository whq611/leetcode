public class l198_1 {
    public int rob(int[] nums) {
        if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];
        //Integer[] res = new Integer[nums.length];
        int slow = nums[0];
        int fast = Math.max(nums[0], nums[1]);
        for(int i=2; i<nums.length; i++){
            int tmp = Math.max(slow+nums[i], fast);
            slow = fast;
            fast = tmp;
        }
        return fast;
    }
}
