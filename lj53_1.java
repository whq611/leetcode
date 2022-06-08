public class lj53_1 {
    public int search(int[] nums, int target) {
        
        return help(nums,target) - help(nums,target-1);
        
    }
    private int help(int[] nums, int target){
        int l = 0, r = nums.length-1;
        while(l<=r){
            int m = l+(r-l)/2;
            if(nums[m]>target) r = m-1;
            else l = m+1;
        }
        return l;
    }
}
