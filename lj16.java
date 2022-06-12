public class lj16 {
    public double myPow(double x, int n) {
        long b=n;
        if(b==0) return 1;
        if(b<0) return 1/myPoww(x,-b);
        else{
            if(b%2==0) return myPoww(x*x,b/2);
            else return myPoww(x*x,b/2)*x;
        }
    }
    public double myPoww(double x, long b){
        if(b==0) return 1;
        if(b<0) return 1/myPoww(x,-b);
        else{
            if(b%2==0) return myPoww(x*x,b/2);
            else return myPoww(x*x,b/2)*x;
    }
}
}