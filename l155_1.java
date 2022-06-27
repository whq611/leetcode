import java.util.Stack;

public class l155_1 {
    Stack<Long> a;
    long b;
    public l155_1() {
        a = new Stack<Long>();
        b = 0L;
    }
    
    public void push(int val) {
        if(a.isEmpty()){
            a.push(0L);
            b = (long) val;
        }else{
            long diff = (long)val - b;
            a.push(diff);
            if(diff<0) b = (long)val;
        }
    }
    
    public void pop() {
        long diff = a.pop();
        if(diff<0){
            long top =  b;
            b = b-diff;
        }
        
    }
    
    public int top() {
        if(a.peek()<0) return (int) b;
        else return (int)(b+a.peek());
    }
    
    public int getMin() {
        return (int)b;
    }
}
