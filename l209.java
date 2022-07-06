public class l209 {
    public int minSubArrayLen(int target, int[] nums) {
        int res = nums.length+1, l = 0, r = 0, summ = 0;
        while(l<=r && r<nums.length){
            summ+=nums[r];
            while(l<=r && summ>=target){
                res = Math.min(res, r-l+1);
                summ-=nums[l];
                l++;
            }
            r++;
        }
        if(res==nums.length+1) return 0;
        return res;
    }
}
