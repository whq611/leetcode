import java.util.HashMap;

public class l1 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> dict = new HashMap<>();
        int[] res = new int[2];
        for(Integer i = 0; i < nums.length; i++){
            if(dict.containsKey(target - nums[i])){
                res[0] = dict.get((target - nums[i]));
                res[1] = i;
                return res;
            }
            dict.put(nums[i],i);
        }
        return res;
    }
}
