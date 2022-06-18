public class l415 {
    public String addStrings(String num1, String num2) {
        StringBuilder res = new StringBuilder();
        int a = 0, i = num1.length()-1, j = num2.length()-1;
        while(i>=0 || j>=0 || a!=0){
            if(i>=0) a+=(num1.charAt(i)-'0');
            if(j>=0) a+=(num2.charAt(j)-'0');
            res.append(String.valueOf(a%10));
            a /= 10;
            i-=1;
            j-=1;
        }
        return res.reverse().toString();
    }
}
