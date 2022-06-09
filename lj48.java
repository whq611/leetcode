import java.util.HashMap;

public class lj48 {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> a = new HashMap<>();
        int cur=0, pre=0, res=0;
        char[] b = s.toCharArray();
        for(int i=0; i<b.length; i++){
            if(a.containsKey(b[i])) cur = Math.min(pre+1,i-a.get(b[i]));
            else cur = pre+1;
            res = Math.max(res,cur);
            pre = cur;
            a.put(b[i],i);

        }
        return res;
    }
}
