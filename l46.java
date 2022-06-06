import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class l46 {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if(nums.length==0) return res;
        LinkedList<Integer> path = new LinkedList<>();
        dfs(path, res, nums);
        return res;
    }
    private void dfs( LinkedList<Integer> path, List<List<Integer>> res, int[] nums){
        if(path.size()==nums.length){
            res.add(new ArrayList<>(path));
            return;
        }
        for(int i=0; i<nums.length; i++){
            if(!path.contains(nums[i])){
                path.add(nums[i]);
                dfs(path,res, nums);
                path.removeLast();
            }
        }
    }
}
