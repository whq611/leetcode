import java.util.Arrays;

public class l213 {
    public int rob(int[] nums) {
        if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];
        return Math.max(myrob(Arrays.copyOfRange(nums, 0, nums.length-1)), myrob(Arrays.copyOfRange(nums, 1, nums.length)));
    }

    public int myrob(int[] nums){
        if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];
        Integer[] res = new Integer[nums.length];
        res[0] = nums[0];
        res[1] = Math.max(nums[0], nums[1]);
        for(int i=2; i<nums.length; i++) res[i] = Math.max(res[i-2]+nums[i], res[i-1]);
        return res[nums.length-1];
    }
}
