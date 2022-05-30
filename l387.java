
import java.util.HashMap;

public class l387 {
    public int firstUniqChar(String s) {
        HashMap<Character,Integer> a = new HashMap<>();
        for(int i=0; i<s.length();i++){
            if(a.containsKey(s.charAt(i))) a.put(s.charAt(i),a.get(s.charAt(i))+1);
            else a.put(s.charAt(i),1);
        }
        for(int i=0; i<s.length();i++){
            if(a.get(s.charAt(i))==1) return i;
        }
        return -1;
    }
}
