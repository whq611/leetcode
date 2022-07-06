public class l713 {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int res = 0, l = 0, r = 0, a = 1;
        while(l<=r && r<nums.length){
            a*=nums[r];
            while(l<=r && a>=k){
                a/=nums[l];
                l++;
            }
            res+=r-l+1;
            r++;
        }
        return res;
    }
}
