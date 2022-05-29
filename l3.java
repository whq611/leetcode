import java.util.Arrays;
import java.util.HashMap;

public class l3 {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()==0) return 0;
        HashMap<Character,Integer> dict = new HashMap<>();
        
        int[] a = new int[s.length()];
        for(int i=0;i<s.length();i++){
            if(i==0) a[i] = 1;
            else if(dict.containsKey(s.charAt(i))){
                a[i] = Math.min(a[i-1]+1,i-dict.get(s.charAt(i)));
            
            }else{
                a[i] = a[i-1] + 1;
                
            }
            dict.put(s.charAt(i),i);
        }
        return Arrays.stream(a).max().getAsInt();
    }
}
