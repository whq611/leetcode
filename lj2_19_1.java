public class lj2_19_1 {
    public boolean validPalindrome(String s) {
        for(int i=0; i<s.length(); i++){
            String a = s.substring(0,i) + s.substring(i+1);
            String b = new StringBuffer(a).reverse().toString();
            if(a.equals(b)) return true;
        }
        return false;
    }
}
