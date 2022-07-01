import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.List;
public class lj2_7_1 {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> res = new HashSet<>();
        Set<Integer> dups = new HashSet<>();
        Map<Integer,Integer> seen = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            if(dups.add(nums[i])){
                for(int j=i+1; j<nums.length; j++){
                    int c = -nums[i]-nums[j];
                    if(seen.containsKey(c) && seen.get(c)==i){
                        List<Integer> t = Arrays.asList(nums[i],nums[j],c);
                        Collections.sort(t);
                        res.add(t);
                    }
                    seen.put(nums[j],i);
                }
            }
        }
        return new ArrayList<>(res);
    
    }
}
