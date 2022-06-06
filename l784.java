import java.util.ArrayList;
import java.util.List;

public class l784 {
    public List<String> letterCasePermutation(String s) {
        List<String> res = new ArrayList<>();
        if(s.length()==0) return res;
        StringBuilder ss=new StringBuilder(s);
        dfs(0,ss,res);
        return res;
    }

    public void dfs(int a, StringBuilder ss, List<String> res){
        if(a==ss.length()){
            res.add(ss.toString());
            return;
        }
        for(int i=a; i<ss.length(); i++){
            if(Character.isLetter(ss.charAt(i))){
                ss.setCharAt(i, Character.toUpperCase(ss.charAt(i)));
                dfs(i+1,ss,res);
                ss.setCharAt(i, Character.toLowerCase(ss.charAt(i)));
            }
            if(i==ss.length()-1){
            res.add(ss.toString());
            return;
        }
    }
}
}
