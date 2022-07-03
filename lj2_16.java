import java.util.HashMap;
import java.util.Map;
public class lj2_16 {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()==0) return 0;
        int res = 1, pre = 1;
        Map<Character, Integer> a = new HashMap<>();
        a.put(s.charAt(0), 0);
        for(int i=1; i<s.length(); i++){
            if(!a.containsKey(s.charAt(i))) pre++;
            else pre = Math.min(pre+1, i-a.get(s.charAt(i)));
            res = Math.max(res,pre);
            a.put(s.charAt(i), i);
        }
        return res;
    }
}
