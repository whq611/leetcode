import java.util.ArrayList;
import java.util.List;


public class lj_2_51_1 {
    public int reversePairs(int[] nums) {
        List<Integer> q = new ArrayList<>();
        int res = 0;
        for(Integer v: nums){
            int l = 0, r = q.size()-1;
            if(l>r){
                q.add(-v);
                continue;
            }
            
            while(l<=r){
                int m = (l+r)/2;
                if(q.get(m)<-v) l = m+1;
                else r = m-1;
            }
            res+=l;
            q.add(l,-v);
        }
        return res;
    }
}
