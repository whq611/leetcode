import java.util.HashMap;

public class l409 {
    public int longestPalindrome(String s) {
        HashMap<Character,Integer> a = new HashMap<>();
        int res = 0;
        for(char i: s.toCharArray()){
            if(a.containsKey(i)) a.put(i,a.get(i)+1);
            else a.put(i,1);
        }
        boolean b = false;
        for(Integer val: a.values()){
            if(val%2==0) res+=val;
            else{
                b = true;
                res+=val-1;
            }
        }
        if(b) return res+1;
        else return res;
    }
}
