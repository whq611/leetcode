import java.util.HashSet;

public class lj03 {
    public int findRepeatNumber(int[] nums) {
        HashSet<Integer> a = new HashSet<Integer>();
        for(int i: nums){
            if(a.contains(i)) return i;
            a.add(i);
        }
        return -1;
    }
}
