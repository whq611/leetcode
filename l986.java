import java.util.ArrayList;
import java.util.List;
public class l986 {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> res = new ArrayList<>();
        int i = 0, j = 0;
        while(i<firstList.length && j<secondList.length){
            if(firstList[i][1]<secondList[j][0]){
                i+=1;
                continue;
            }
            if(secondList[j][1]<firstList[i][0]){
                j+=1;
                continue;
            }
            int [] tmp = new int[2];
            tmp[0] = Math.max(firstList[i][0],secondList[j][0]);
            tmp[1] = Math.min(firstList[i][1], secondList[j][1]);
            res.add(tmp);
            if(firstList[i][1]>secondList[j][1]) j+=1;
            else if(firstList[i][1]<secondList[j][1]) i+=1;
            else{
                i+=1;
                j+=1;
            }
        }
        return res.toArray(new int[res.size()][2]);
    }
}
