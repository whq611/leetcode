public class l34 {
    public int[] searchRange(int[] nums, int target) {
        if(nums.length==0) return new int[]{-1,-1};
        int i = dfs(nums,target);
        int j = dfs(nums,target+1);
        if(i==j) return new int[]{-1,-1};
        return new int[]{i+1,j};
    }
    public int dfs(int[] nums, int target){
        int l = 0, r = nums.length-1;
        while(l<=r){
            int m = l+(r-l)/2;
            if(nums[m]>=target) r = m-1;
            else l = m+1;
        }
        return r;
    }
}
