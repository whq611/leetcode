import java.util.ArrayList;
import java.util.HashMap;

public class l350 {
    public int[] intersect(int[] nums1, int[] nums2) {
        ArrayList<Integer> res = new ArrayList<>();
        HashMap<Integer,Integer> dict = new HashMap<>();
        for(int i: nums1){
            if(dict.containsKey(i)) dict.put(i,dict.get(i)+1);
            else dict.put(i,1);
        }
        for(int i:nums2){
            if(dict.containsKey(i) && dict.get(i)!=0){
                dict.put(i,dict.get(i)-1);
                res.add(i);
            }
        }
        int[] ans = new int[res.size()];
        for(int i=0;i<res.size();i++) ans[i] = res.get(i);
        return ans;
    } 
}
