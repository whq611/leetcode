import java.util.Arrays;

public class l88_1 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] nums1_copy = Arrays.copyOfRange(nums1,0,m);
        int p1 = 0, p2 = 0;
        for(int p=0; p<m+n;p++){
            if(p2==n || (p1<m && nums1_copy[p1]<=nums2[p2])) nums1[p] = nums1_copy[p1++]; else nums1[p] = nums2[p2++];
        }
    }
}
