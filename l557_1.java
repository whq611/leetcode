public class l557_1 {
    public String reverseWords(String s) {
        StringBuilder res = new StringBuilder();
        StringBuilder word = new StringBuilder();
        for(char i: s.toCharArray()){
            if(i != ' ') word.append(i);
            else{
                res.append(word.reverse());
                res.append(" ");
                word.setLength(0);
            }
        }
        res.append(word.reverse());
        return res.toString();
    }
}
