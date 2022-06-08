public class lj03_2 {
    public int findRepeatNumber(int[] nums) {
        int i = 0;
        while(i<nums.length){
            if(nums[i]==i){
                i++;
                continue;
            }
            if(nums[i]==nums[nums[i]]) return nums[i];
            int tmp = nums[i];
            nums[i] = nums[nums[i]];
            nums[tmp] = tmp;
        }

        return -1;
    }
}
