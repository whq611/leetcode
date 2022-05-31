import java.util.HashMap;
import java.util.Map;

public class l167 {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer,Integer> a = new HashMap<>();
        for(int i=0;i<numbers.length;i++){
            if(a.containsKey(target-numbers[i])) return new int[] {a.get(target-numbers[i])+1,i+1};
            a.put(numbers[i],i);
        }
        return null;
    }
}
