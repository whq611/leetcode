import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
public class lj2_7 {
    int n;
    int[] nums;
    List<List<Integer>> res;
    public List<List<Integer>> threeSum(int[] nums) {
        this.res = new ArrayList<>();
        this.nums = nums;
        this.n = nums.length;
        Arrays.sort(nums);
        for(int i=0; i<n; i++){
            if((i==0 || nums[i]!=nums[i-1]) && nums[i]<=0) twoSum(i,-nums[i]);
        }
        return res;
    }
    public void twoSum(int i, int target){
        int l=i+1, r = n-1;
        while(l<r){
            if(l>i+1 && nums[l]==nums[l-1]) l++;
            else if(nums[l]+nums[r]==target){
                List<Integer> a = new ArrayList<>();
                a.add(nums[i]);
                a.add(nums[l]);
                a.add(nums[r]);
                res.add(a);
                l++;
                r--;
            }
            else if(nums[l]+nums[r]<target) l++;
            else r--;
        }
    }
}
