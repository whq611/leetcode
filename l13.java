import java.util.HashMap;
public class l13 {
    public int romanToInt(String s) {
        HashMap<Character, Integer> dict = new HashMap<>();
        
        dict.put('I', 1);
        dict.put('V', 5);
        dict.put('X', 10);
        dict.put('L', 50);
        dict.put('C', 100);
        dict.put('D', 500);
        dict.put('M', 1000);
        int res = 0;
        for(int i=0; i<s.length(); i++){
            if(i != s.length()-1 && dict.get(s.charAt(i)) < dict.get(s.charAt(i+1))){
                res -= dict.get(s.charAt(i));
            }else res += dict.get(s.charAt(i));
        }
        return res;
    }
}
