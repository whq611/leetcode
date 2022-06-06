import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class l46_2 {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if(nums.length==0) return res;
        ArrayList<Integer> nums_lst = new ArrayList<Integer>();
        for (int num : nums) nums_lst.add(num);
        dfs(0, nums_lst, res);
        return res;
    }
    private void dfs(int index, ArrayList<Integer> nums, List<List<Integer>> res){
        if(index==nums.size()){
            res.add(new ArrayList<>(nums));
            return;
        }
        for(int i=index; i<nums.size(); i++){
            Collections.swap(nums, index, i);
            dfs(index+1, nums, res);
            Collections.swap(nums, index, i);
            
        }
    }
}
