public class l283 {
    public void moveZeroes(int[] nums) {
        int j = 0;
        for(int i:nums){
            if(i!=0){
                nums[j] = i;
                j+=1;
            }
        }
        for(int i=j;i<nums.length;i++){
            nums[i] = 0;
        }
    }
}
