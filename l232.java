import java.util.Stack;

public class l232 {
    Stack<Integer> a;
    Stack<Integer> b;
    public l232() {
        a = new Stack();
        b = new Stack();
    }
    
    public void push(int x) {
        a.push(x);
    }
    
    public int pop() {
        if(!b.isEmpty()) return b.pop();
        while(!a.isEmpty()) b.push(a.pop());
        return b.pop();
    }
    
    public int peek() {
        if(!b.isEmpty()) return b.peek();
        while(!a.isEmpty()) b.push(a.pop());
        return b.peek();
    }
    
    public boolean empty() {
        return a.isEmpty() && b.isEmpty();
    }
}
