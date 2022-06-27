public class l1249 {
    public String minRemoveToMakeValid(String s) {
        StringBuilder tmp = new StringBuilder();
        StringBuilder res = new StringBuilder();
        int l=0, r=0;
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)=='(') l++;
            if(s.charAt(i)==')'){
                if(l==0) continue;
                l--;
            }
            tmp.append(s.charAt(i));
        }
        for(int j=tmp.length()-1; j>=0; j--){
            if(tmp.charAt(j)==')') r++;
            if(tmp.charAt(j)=='('){
                if(r==0) continue;
                r--;
            }
            res.append(tmp.charAt(j));
        }
        return res.reverse().toString();
    }
}
