public class lj46_1 {
    public int translateNum(int num) {
        
        int a = 1, b = 1;
        int c;
        int x = num%10;
        int y;
        while(num!=0){
            num /= 10;
            y = num%10;
            if(10*y+x<=25 && 10*y+x>=10) c = a+b;
            else c = b;
            x = y;
            a = b;
            b = c;
        }
        return b;
    }
}
