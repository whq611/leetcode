public class l557 {
    public String reverseWords(String s){
        String words[] = s.split(" ");
        StringBuilder res = new StringBuilder();
        for(String word: words){
            res.append(new StringBuilder(word).reverse().toString() + " ");
        }
        return res.toString().trim();
    }
}
