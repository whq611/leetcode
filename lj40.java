import java.util.Arrays;
import java.util.Random;

public class lj40 {
    public int[] getLeastNumbers(int[] arr, int k) {
        quick_sort(arr,0,arr.length-1);
        int[] res = Arrays.copyOfRange(arr, 0, k);
        return res;
    }

    private void quick_sort(int[] arr, int l, int r){
        if(l>=r) return;
        int a = new Random().nextInt(r-l+1)+l;
        swap(arr,a,r);
        int i = l, j = l;
        while(j<r){
            if(arr[j]<=arr[r]){
                swap(arr,i,j);
                i++;
            }
            j++;
        }
        swap(arr,i,r);
        quick_sort(arr,l,i-1);
        quick_sort(arr,i+1,r);
    }

    private void swap(int[] arr, int l, int r){
        int tmp = arr[l];
        arr[l] = arr[r];
        arr[r] = tmp;
    }
}
