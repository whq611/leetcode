public class l75 {
    public void sortColors(int[] nums) {
        int l = 0, cur = 0, r = nums.length-1;
        while(cur<=r){
            if(nums[cur]==0){
                int tmp = nums[cur];
                nums[cur] = nums[l];
                nums[l] = tmp;
                l++;
                cur++;
            }
            else if(nums[cur]==2){
                int tmp = nums[cur];
                nums[cur] = nums[r];
                nums[r] = tmp;
                r--;
                
            }
            else cur++;
        }

    }
}
