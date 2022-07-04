public class l844 {
    public boolean backspaceCompare(String s, String t) {
        int i = s.length()-1, j = t.length()-1, a=0;
        while(i>=0 || j>=0){
        while((i>=0 && s.charAt(i)=='#') || a!=0){
            if(i>=0 && s.charAt(i)=='#'){
                i--;
                a++;
            }
            else{
                i--;
                a--;
            }
        }
        while((j>=0 && t.charAt(j)=='#') || a!=0){
            if(j>=0 && t.charAt(j)=='#'){
                j--;
                a++;
            }
            else{
                j--;
                a--;
            }
        }
        if(i>=0 && j>=0){
            if(s.charAt(i)==t.charAt(j)){
                i--;
                j--;
            }
            else return false;
        }
        else if(i>=0 || j>=0) return false;
        }
        return i<0 && j<0;
    }
}
