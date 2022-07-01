public class lj2_6 {
    public int[] twoSum(int[] numbers, int target) {
        int[] res = new int[2];
        int i=0, j = numbers.length-1;
        while(i<j){
            if(numbers[i]+numbers[j]==target) break;
            else if(numbers[i]+numbers[j]<target) i++;
            else j--;
        }
        res[0]=i;
        res[1]=j;
        return res;
    }
}
