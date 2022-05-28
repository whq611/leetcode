public class l42_1 {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length-1;
        int res = 0;
        int leftMax = 0, rightMax = 0;
        while(left<right){
            leftMax = Math.max(leftMax,height[left]);
            rightMax = Math.max(rightMax,height[right]);
            if(height[left] <= height[right]){
                res += leftMax - height[left];
                left += 1;
            }else{
                res += rightMax - height[right];
                right -= 1;
            }
        }
        return res;
}
}
