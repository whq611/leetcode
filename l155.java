import java.util.Stack;

public class l155 {
    Stack<Integer> a;
    Stack<Integer> b;
    public l155() {
        a = new Stack<Integer>();
        b = new Stack<Integer>();
    }
    
    public void push(int val) {
        a.push(val);
        if(b.isEmpty() || b.peek()>=val){
            b.push(val);
        }
    }
    
    public void pop() {
        int tmp = a.pop();
        if(!b.isEmpty() && b.peek()==tmp) b.pop();
    }
    
    public int top() {
        return a.peek();
    }
    
    public int getMin() {
        return b.peek();
    }
}
