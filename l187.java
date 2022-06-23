import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.List;
public class l187 {
    public List<String> findRepeatedDnaSequences(String s) {
        if(s.length()<=10) return new ArrayList<>();
        Set<String> sites = new HashSet<String>();
        Set<String> ans = new HashSet<String>();
        for(int i = 10; i<s.length()+1; i++){
            if(sites.contains(s.substring(i-10,i))) ans.add(s.substring(i-10,i));
            sites.add(s.substring(i-10,i));
        }
        return new ArrayList<>(ans);
    }
}
