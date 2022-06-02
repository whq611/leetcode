public class l557_2 {
    public String reverseWords(String s) {
        int n = s.length();
        char[] cs = s.toCharArray();
        int lo = 0, hi = 0;
        while(hi<n){
            while(hi<n && cs[hi] != ' '){
                hi++;
            }
            reverse(cs, lo, hi-1);
            hi++;
            lo = hi;
    }
    return new String(cs);
}
void reverse(char[] cs, int lo, int hi){
    while(lo<hi){
        char c = cs[lo];
        cs[lo] = cs[hi];
        cs[hi] = c;
        lo++;
        hi--;
    }
}
}
