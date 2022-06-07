public class l190 {
    public int reverseBits(int n) {
        int rev = 0;
        int a = 31;
        while(a>=0){
            rev |= (n&1)<<a;
            n>>=1;
            a -= 1;
        }
        return rev;


    }
}
