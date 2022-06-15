import java.util.ArrayList;
import java.util.List;
public class l119 {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> cur = new ArrayList<Integer>();
        cur.add(1);
        List<Integer> pre = new ArrayList<Integer>();
        while(rowIndex>=1){
            cur = new ArrayList<Integer>();
            
            cur.add(1);
            for(int i=0; i<pre.size()-1;i++){
                cur.add(pre.get(i) + pre.get(i+1));
            }
            cur.add(1);
            pre.clear();
            rowIndex-=1;
            pre = cur;
        }
        return cur;
    }
}
