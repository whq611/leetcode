public class lj11 {
    public int minArray(int[] numbers) {
        int l = 0, r = numbers.length-1;
        while(l<r){
            int m = l + (r-l)/2;
            if(numbers[m]>numbers[r]) l = m+1;
            else if(numbers[m]<numbers[r]) r = m;
            else r-=1;
        }
        return numbers[l];

    }
}
