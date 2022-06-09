import java.util.Arrays;

public class lj42 {
    public int maxSubArray(int[] nums) {
        int[] res = new int[nums.length];
        res[0] = nums[0];
        for(int i=1; i<nums.length; i++){
            res[i] = Math.max(nums[i], nums[i]+res[i-1]);
        }
        return Arrays.stream(res).max().getAsInt();
    }
}
