public class lj53 {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length-1;
        while(l<=r){
            int m = l + (r-l)/2;
            if(nums[m]>=target) r = m-1;
            else l = m+1;
        }
        int left = r;
        l = 0;
        r = nums.length-1;
        while(l<=r){
            int m = l + (r-l)/2;
            if(nums[m]>target) r = m-1;
            else l = m+1;
        }
        int right = l;
        return right-left-1;
    }
}
