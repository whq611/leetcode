public class lj2_12 {
    public int pivotIndex(int[] nums) {
        int pre = 0;
        int[] a = new int[nums.length+1];
        for(int i=0; i<nums.length; i++){
            pre+=nums[i];
            a[i+1] = pre;
        }
        for(int i=0; i<nums.length; i++){
            if(a[i]*2 == pre-nums[i]) return i;
        }
        return -1;
    }
}
