public class l191_1 {
    public int hammingWeight(int n) {
        int res = 0;
        for(int i=0; i<32; i++){
            if ((n & (1 << i)) != 0) res+=1;
        }
        return res;
        


    }
}
