import java.util.HashMap;
import java.util.Map;

public class l242 {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> a = new HashMap<>();
        for(char c: s.toCharArray()){
            int i = a.getOrDefault(c,0);
            a.put(c,i+1);
        }
        for(char c: t.toCharArray()){
            if(!a.containsKey(c) || a.get(c)<1) return false;
            if(a.get(c)-1 == 0) a.remove(c);
            else a.put(c,a.get(c)-1);

        }
        return a.isEmpty();
    }
}
