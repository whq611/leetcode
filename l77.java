
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;


public class l77 {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        if (k <= 0 || n < k) {
            return res;
        }
        LinkedList<Integer> path = new LinkedList<>();
        dfs(n, k, 1, path, res);
        return res;
    }

    private void dfs(int n, int k, int index, LinkedList<Integer> path, List<List<Integer>> res) {
        if (path.size() == k) {
            res.add(new ArrayList<>(path));
            return;
        }

        // 只有这里 i <= n - (k - path.size()) + 1 与参考代码 1 不同
        for (int i = index; i <= n - (k - path.size()) + 1; i++) {
            path.add(i);
            dfs(n, k, i + 1, path, res);
            path.removeLast();
        }
    }


}
