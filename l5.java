public class l5 {
    public String longestPalindrome(String s) {
        StringBuffer res = new StringBuffer("");
        for(int i=0; i<s.length(); i++){
            for(int j=0; j<=i; j++){
                if(i-j+1<=res.length()) break;
                StringBuffer a = new StringBuffer(s.substring(j,i+1));
                String b = a.reverse().toString();
                if(b.equals(s.substring(j,i+1))){
                    res = new StringBuffer(s.substring(j,i+1));
                    break;
                }
            }
        }
        return res.toString();
    }
}
