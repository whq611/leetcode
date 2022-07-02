import java.util.HashMap;
import java.util.Map;

public class lj_2_10 {
    public int subarraySum(int[] nums, int k) {
        int res=0, pre=0;
        if(nums.length==0) return res;
        Map<Integer,Integer> a = new HashMap<>();
        a.put(0,1);
        for(int num: nums){
            pre+=num;
            res+=a.getOrDefault(pre-k,0);
            a.put(pre,a.getOrDefault(pre, 0) + 1);
        }
        return res;
    }
}
