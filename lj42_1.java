public class lj42_1 {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int pre = nums[0];
        for(int i=1; i<nums.length; i++){
            int cur = Math.max(nums[i], nums[i]+pre);
            res = Math.max(res,cur);
            pre = cur;
        }
        return res;
    }
}
