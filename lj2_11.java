import java.util.HashMap;
import java.util.Map;

public class lj2_11 {
    public int findMaxLength(int[] nums) {
        Map<Integer,Integer> a = new HashMap<>();
        int b=0, res=0;
        a.put(0,-1);
        for(int i=0; i<nums.length; i++){
            if(nums[i]==1) b++;
            else b--;
            if(a.containsKey(b)) res = Math.max(res,i-a.get(b));
            else a.put(b,i);
        }
        return res;
    }
}
