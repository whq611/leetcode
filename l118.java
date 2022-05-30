import java.util.ArrayList;
import java.util.List;

public class l118 {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> a = new ArrayList<Integer>();
        a.add(1);
        res.add(a);

        while(numRows>1){
            List<Integer> cur = new ArrayList<>();
            List<Integer> pre = res.get(res.size()-1);
            cur.add(1);
            for(int i=0; i<pre.size()-1;i++) cur.add(pre.get(i) + pre.get(i+1));
            cur.add(1);
            res.add(cur);
            numRows-=1;
        }
        return res;

        
        
    }
}
