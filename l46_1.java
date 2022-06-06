import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class l46_1 {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if(nums.length==0) return res;
        LinkedList<Integer> path = new LinkedList<>();
        boolean[] used = new boolean[nums.length];
        dfs(path, res, nums, used);
        return res;
    }
    private void dfs( LinkedList<Integer> path, List<List<Integer>> res, int[] nums,boolean[] used){
        if(path.size()==nums.length){
            res.add(new ArrayList<>(path));
            return;
        }
        for(int i=0; i<nums.length; i++){
            if(!used[i]){
                path.add(nums[i]);
                used[i] = true;
                dfs(path,res, nums, used);
                path.removeLast();
                used[i] = false;
            }
        }
    }
}
