public class lj46 {
    public int translateNum(int num) {
        String s = String.valueOf(num);
        int a = 1, b = 1;
        int c;
        for(int i=2; i<s.length()+1; i++){
            if(s.substring(i-2,i).compareTo(String.valueOf(25))<=0 && s.substring(i-2,i).compareTo(String.valueOf(10))>=0) c = a+b;
            else c = b;
            a = b;
            b = c;
        }
        return b;
    }
}
