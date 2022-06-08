public class lj_2_53 {
    public int missingNumber(int[] nums) {
        int l=0, r=nums.length-1;
        while(l<=r){
            int m = l+(r-l)/2;
            if(nums[m]==m) l = m+1;
            else r = m-1;
        }
        return l;
    }
}
