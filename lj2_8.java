public class lj2_8 {
    public int minSubArrayLen(int target, int[] nums) {
        
        int n = nums.length, res = n+1, b=0, i=1;
        if(n==0) return 0;
        int[] a = new int[n+1];
        for(int num: nums){
            b+=num;
            a[i] = b;
            i++;
        }
        int l=0, r=0;
        while(l<=r && r<=n){
            while(r<=n && a[r]-a[l]<target){
                r++;
            }
            res = Math.min(res,r-l);
            l++;
        }
        if(res==n+1) return 0;
        return res;
    }
}
