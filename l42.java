public class l42 {
    public int trap(int[] height) {
        int[] left = new int[height.length];
        int[] right = new int[height.length];
        int res = 0;
        int leftMax = height[0], rightMax = height[height.length-1];
        for(int i=1; i<height.length; i++){
            leftMax = Math.max(leftMax,height[i]);
            left[i] = leftMax - height[i];
        }
        for(int i=height.length-2; i>=0; i--){
            rightMax = Math.max(rightMax,height[i]);
            right[i] = rightMax - height[i];
        }
        for(int i=0; i<height.length; i++){
            res += Math.min(left[i],right[i]);
        }
        return res;
    }
}
