public class lj2_9 {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int n = nums.length, res = 0, product = 1, l=0, r=0;
        if(n==0) return 0;
        while(l<=r && r<n){
            product *= nums[r];
            while(l<=r && product>=k){
                product /= nums[l];
                l++;
            }
            res+=r-l+1;
            r++;
        }
        return res;
    }
}
