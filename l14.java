public class l14 {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length==0) return "";
        String pre = strs[0];
        for(int i=1; i<strs.length; i++){
            int l = Math.min(pre.length(), strs[i].length());
            int j = 0;
            while(j<l && pre.charAt(j) == strs[i].charAt(j)){
                j++;
            }
            pre = pre.substring(0,j);
            if(pre.length()==0) break;
        }
        return pre;
    }

}
