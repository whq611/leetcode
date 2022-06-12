
import java.util.PriorityQueue;

public class lj41 {
    // 大顶堆存储较小一半的值
    PriorityQueue<Integer> maxHeap;
    // 小顶堆存储较大一般的值
    PriorityQueue<Integer> minHeap;
    /** initialize your data structure here. 
     * @return */
    public void MedianFinder() {
        maxHeap = new PriorityQueue<Integer>((x, y) -> (y - x));
        minHeap = new PriorityQueue<Integer>();
        
    }
    
    public void addNum(int num) {
        // 长度为奇数时先放入小顶堆,重新排序后在插入到大顶堆
        if(maxHeap.size() != minHeap.size()) {
            minHeap.add(num);
            maxHeap.add(minHeap.poll());
        } else {
            // 长度为偶数时先放入大顶堆,重新排序后在插入到小顶堆
            maxHeap.add(num);
            minHeap.add(maxHeap.poll());
        }
    }
    
    public double findMedian() {
        if(maxHeap.size() != minHeap.size()) {
            return minHeap.peek();
        } else {
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
    }




}
