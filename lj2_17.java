public class lj2_17 {
    public String minWindow(String s, String t) {
        int n = s.length(), m = t.length(), k = 0, l=0, r = 0, i = 0;
        if(n<m) return "";
        int[] cnt = new int[150];
        for(char c: t.toCharArray()){
            cnt[c]+=1;
            if(cnt[c]==1) k++;
        }
        for(int j = 0; j<n; j++){
            char c = s.charAt(j);
            cnt[c]--;
            if(cnt[c]==0) k--;
            if(k==0){
                while(cnt[s.charAt(i)]<0){
                    cnt[s.charAt(i)]++;
                    i++;
                }
                if(l==r || j-i+1<r-l){
                    r = j+1;
                    l = i;
                }
            }
        }
        return s.substring(l,r);
    }
}
