import java.util.HashMap;
import java.util.Map;

public class l383 {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character,Integer> a = new HashMap<>();
        for(char c: magazine.toCharArray()){
            int i = a.getOrDefault(c,0);
            a.put(c,i+1);
        }
        for(char c: ransomNote.toCharArray()){
            if(!a.containsKey(c) || a.get(c)<1) return false;
            a.put(c,a.get(c)-1);

        }
        return true;
    }
}
