public class l33 {
    public int search(int[] nums, int target) {
        if(nums.length==0) return -1;
        int l = 0, r = nums.length-1;
        while(l<=r){
            int m = l + (r-l)/2;
            if(nums[m]==target) return m;
            if(nums[0]<=nums[m]){
                if(nums[l]<=target && target<nums[m]) r = m-1;
                else l = m+1;
            }
            else{
                if(nums[m]<target && target<=nums[r]) l = m+1;
                else r = m-1;
            }
        }
        return -1;
    }
}
