public class lj59 {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(k==0)return new int[0];
        int[] ans = new int[nums.length-k+1];
        for(int i=0; i+k-1<nums.length; i++){
            if(i>0 && nums[i+k-1]>ans[i-1]) ans[i] = nums[i+k-1];
            else if(i>0 && nums[i-1]<ans[i-1]) ans[i] = ans[i-1];
            else{
                int max = Integer.MIN_VALUE;
                for(int j=i; j<i+k; j++){
                    max = Math.max(max,nums[j]);
                    ans[i] = max;
                }
            }
        }
        return ans;
    }
}
