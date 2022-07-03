import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
public class lj2_15 {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        if(p.length() > s.length()){
            return res;
        }
        int[] a = new int[26];
        int[] b = new int[26];
        for(int i = 0;i < p.length();i++){
            a[p.charAt(i) - 'a']++;
            b[s.charAt(i) - 'a']++;
        }
        if(Arrays.equals(a,b)){
            res.add(0);
        } 
        int left = 0,right = p.length();
        while(right < s.length()){
            b[s.charAt(right) - 'a']++;
            b[s.charAt(left) - 'a']--;
            
            right++;
            left++;
            if(Arrays.equals(a,b)){
                res.add(left);
            }
        }
        return res;
    }
}
